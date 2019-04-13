from rest_framework.filters import OrderingFilter
from .exceptions import InvalidAPIQuery


class CustomOrderingFilter(OrderingFilter):
    ordering_param = 'order'

    def get_ordering(self, request, queryset, view):
        params = request.query_params.get(self.ordering_param)
        if params:
            fields = [param.strip() for param in params.split(',')]
            ordering = self.remove_invalid_fields(queryset, fields, view, request)
            if fields != ordering:
                raise InvalidAPIQuery
            else:
                return ordering

        return self.get_default_ordering(view)
