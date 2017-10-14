# -:- coding:utf8 -:-
"""
Customer Parser
"""
from flask_restful.reqparse import Argument
from flask_restful.reqparse import RequestParser
from six import add_metaclass
from six import iteritems


class DeclarativeMeta(type):
    def __new__(cls, name, bases, attributes):
        if name == 'EntityBase':
            return type.__new__(cls, name, bases, attributes)

        class_dict = dict()
        parser = RequestParser()
        fields = [(name, field) for name, field in iteritems(attributes) if isinstance(field, Field)]

        field_names = set()
        for name, field in fields:
            parser.add_argument(field)
            field_names.add(name)
            del attributes[name]
        attributes['entity_parser'] = parser
        attributes['entity_fields'] = field_names

        return type.__new__(cls, name, bases, attributes)


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
        instance = cls()  # type: EntityBase
        args = cls.entity_parser.parse_args(req)
        for field in cls.entity_fields:
            setattr(instance, field, args[field])
        if not instance.validate():
            raise ValueError()
        return instance

    def validate(self):
        return True


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
                if success is not True:
                    found = {self.name: success}
                    value = ValueError()
                    break
        return value, found


class Validator(object):
    message = 'error'

    def __call__(self, value):
        """
        validate param
        :param value: 
        :rtype: bool 
        """
        return self.validate(value)

    def validate(self, value):
        raise NotImplementedError()

    @property
    def error_message(self):
        return self.message


class RangeValidator(Validator):
    def __init__(self, min_value=None, max_value=None):
        if None not in (min_value, max_value) and min_value > max_value:
            raise ValueError("min_value must be less than max_value")

        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if self.min_value is not None:
            return self.min_value <= value
        if self.max_value is not None:
            return self.max_value >= value
        return self.min_value <= value <= self.max_value


class Entity(EntityBase):
    Name = Field('Name', location='json', type=int, validators=[RangeValidator(1)])

    def validate(self):
        return self.Name == 8


if __name__ == '__main__':
    class X(object):
        def json(self):
            return {'Name': 8}


    entity = Entity.parse(X())
    print(entity.Name)
    entity.validate()
