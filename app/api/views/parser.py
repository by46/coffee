# -:- coding:utf8 -:-
"""
Customer Parser
"""
import functools
import inspect
from datetime import datetime
from decimal import Decimal

import flask_restful.fields
from flask_kits.restful import post_parameter
from flask_restful import abort
from flask_restful.reqparse import Argument
from flask_restful.reqparse import RequestParser
from flask_restful_swagger import swagger
from six import add_metaclass
from six import iteritems
from six import text_type


def parameter(schema):
    """
    :param EntityBase schema:
    """

    def wrapper(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            entity = schema.parse()
            kwargs['entity'] = entity
            return f(*args, **kwargs)

        # Support swagger document
        if '__swagger_attr' in f.__dict__:
            attr = wrapped.__dict__['__swagger_attr'] = f.__dict__['__swagger_attr']
            params = attr.get('parameters', [])
            params.append(post_parameter(schema))
        return wrapped

    return wrapper


MAPPINGS = {
    int: flask_restful.fields.Integer,
    float: flask_restful.fields.Float,
    str: flask_restful.fields.String,
    datetime: flask_restful.fields.DateTime,
    Decimal: flask_restful.fields.String,
    bool: flask_restful.fields.Boolean
}


def get_field_type(class_type):
    return MAPPINGS.get(class_type)


class DeclarativeMeta(type):
    def __new__(cls, name, bases, attributes):
        if name == 'EntityBase':
            return type.__new__(cls, name, bases, attributes)

        parser = RequestParser()
        fields = [(name, field) for name, field in iteritems(attributes) if isinstance(field, Field)]

        field_names = set()
        resource_fields = dict()
        for name, field in fields:
            if inspect.isclass(field.type) and issubclass(field.type, EntityBase):
                field.type = field.type.parse
            parser.add_argument(field)
            field_names.add(name)
            resource_fields[name] = get_field_type(field.type)
            del attributes[name]
        attributes['entity_parser'] = parser
        attributes['entity_fields'] = field_names
        attributes['resource_fields'] = resource_fields

        schema = type.__new__(cls, name, bases, attributes)
        # support swagger
        swagger.add_model(schema)
        return schema


class WrappedDict(dict):
    def __init__(self, source):
        super(WrappedDict, self).__init__(**source)

    def json(self):
        return self


@add_metaclass(DeclarativeMeta)
class EntityBase(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value

    @classmethod
    def parse(cls, req=None):
        """

        :param req: 
        :rtype: EntityBase
        """
        if req is not None:
            req = WrappedDict(req)
        instance = cls()  # type: EntityBase
        args = cls.entity_parser.parse_args(req)
        for field in cls.entity_fields:
            setattr(instance, field, args[field])
        success = instance.validate()
        if isinstance(success, ValueError):
            abort(400, message={'error': text_type(success)})
        return instance

    def validate(self):
        """
        :rtype: (bool|ValueError)
        """
        return True

    def handle_error(self):
        pass


class Field(Argument):
    def __init__(self, name, *args, **kwargs):
        self.validators = set()
        if 'validators' in kwargs:
            self.validators = kwargs.pop('validators')
        super(Field, self).__init__(name, *args, **kwargs)

    def parse(self, request, bundle_errors=False):
        value, found = super(Field, self).parse(request, bundle_errors)
        if not isinstance(value, ValueError) and self.validators:
            for validator in self.validators:
                success = validator(value)
                if isinstance(success, ValueError):
                    found = {self.name: text_type(success)}
                    value = ValueError()
                    break
        return value, found


class Validator(object):
    help = ""

    def __call__(self, value):
        """
        validate param
        :param value: 
        :rtype: bool 
        """
        return self.validate(value)

    def validate(self, value):
        """
        :rtype: (None|ValueError)
        """
        raise NotImplementedError()

    def handle_error(self, *args):
        return ValueError(self.help.format(*args))


class CompareValidator(Validator):
    def __init__(self, threshold):
        self.threshold = threshold

    def validate(self, value):
        if value is None or self.illegal(value):
            return self.handle_error(self.threshold)

    def illegal(self, value):
        raise NotImplementedError()


class LetterValidator(CompareValidator):
    help = "Must be less than {0}"

    def illegal(self, value):
        return value > self.threshold


class MoreValidator(CompareValidator):
    help = "Must be more than {0}"

    def illegal(self, value):
        return value < self.threshold


class MinLengthValidator(CompareValidator):
    help = "String length must be more than {0}"

    def illegal(self, value):
        return len(value) < self.threshold


class MaxLengthValidator(CompareValidator):
    help = "String length must be less than {0}"

    def illegal(self, value):
        return len(value) > self.threshold


class PrecisionValidator(CompareValidator):
    help = "Must be less than {0} precision bit"

    def illegal(self, value):
        """
        :param Decimal value:
        """
        return value.quantize(Decimal('1.' + (self.threshold * '0'))) != value


class Entity(EntityBase):
    Name = Field('Name', location='json', type=int, validators=[MoreValidator(1), LetterValidator(15)])

    def validate(self):
        return self.Name == 8


if __name__ == '__main__':
    class X(object):
        def json(self):
            return {'Name': 8}


    entity2 = Entity.parse(X())
    print(entity2.Name)
    entity2.validate()
