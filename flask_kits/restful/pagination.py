from functools import wraps

from flask import abort
from flask import has_request_context
from flask import request
from flask_restful import fields
from flask_restful import marshal
from flask_restful import marshal_with
from flask_restful.utils import unpack
from flask_sqlalchemy import BaseQuery
from flask_sqlalchemy import Pagination
from furl import furl


def paginate(query, page=None, per_page=None, error_out=True):
    """Clone from flask_sqlachemy.Pagination
    Returns `per_page` items from page `page`.  By default it will
    abort with 404 if no items were found and the page was larger than
    1.  This behavor can be disabled by setting `error_out` to `False`.

    If page or per_page are None, they will be retrieved from the
    request query.  If the values are not ints and ``error_out`` is
    true, it will abort with 404.  If there is no request or they
    aren't in the query, they default to page 1 and 20
    respectively.

    Returns an :class:`Pagination` object.
    """

    if has_request_context():
        if page is None:
            try:
                page = int(request.args.get('page', 1))
            except (TypeError, ValueError):
                if error_out:
                    abort(404)

                page = 1

        if per_page is None:
            try:
                per_page = int(request.args.get('per_page', 20))
            except (TypeError, ValueError):
                if error_out:
                    abort(404)

                per_page = 20
    else:
        if page is None:
            page = 1

        if per_page is None:
            per_page = 20

    if error_out and page < 1:
        abort(404)

    items = query.limit(per_page).offset((page - 1) * per_page).all()

    if not items and page != 1 and error_out:
        abort(404)

    # No need to count if we're on the first page and there are fewer
    # items than we expected.
    if page == 1 and len(items) < per_page:
        total = len(items)
    else:
        total = query.order_by(None).count()

    return Pagination(query, page, per_page, total, items)


class Paginate(marshal_with):
    """used to pagination

    Example:
        @Paginate({'id'': fields.Integer})
        def get():
            pass

    """

    def __init__(self, serializer_fields, envelope=None, item_builder=None):
        """decorator initialize for Paginate

        :param serializer_fields: a dict of whose keys will make up the final
                       serialized response output
        :param envelope: optional key that will be used to envelop the serialized
                         response
        :param item_builder: optional key that will be used to rebuild item for group_by
        :return:
        """
        super(Paginate, self).__init__(self.rebuild_fields(serializer_fields), envelope=envelope)
        self.item_builder = item_builder

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            resp = func(*args, **kwargs)
            if isinstance(resp, tuple):
                query, code, headers = unpack(resp)
                data = self.make_pagination(query)
                return marshal(data, self.fields, self.envelope), code, headers
            else:
                data = self.make_pagination(resp)
                return marshal(data, self.fields, self.envelope)

        return wrapper

    @staticmethod
    def rebuild_fields(serializer_fields):
        return {
            'count': fields.Integer,
            'previous': fields.String,
            'next': fields.String,
            'results': fields.List(fields.Nested(serializer_fields))
        }

    def make_pagination(self, query):
        if isinstance(query, BaseQuery):
            pagination = query.paginate()
        else:
            pagination = paginate(query)

        if self.item_builder:
            builder = self.item_builder
            pagination.items = [builder(item) for item in pagination.items]

        url = furl(request.url)
        url.args['per_page'] = pagination.per_page
        previous_url = None
        if pagination.has_prev:
            url.args['page'] = pagination.prev_num
            previous_url = url.url

        next_url = None
        if pagination.has_next:
            url.args['page'] = pagination.next_num
            next_url = url.url

        return {
            'count': pagination.total,
            'previous': previous_url,
            'next': next_url,
            'results': pagination.items
        }
