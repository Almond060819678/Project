from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):
    default_limit = 5
    min_limit = 1
    max_limit = 100
    min_offset = 0

    def get_limit(self, request):
        if self.limit_query_param:
            try:
                return self.positive_int(
                    request.query_params[self.limit_query_param],
                    cutoff=self.max_limit
                )
            except ValueError as e:
                raise e
            except KeyError:
                pass

        return self.default_limit

    def get_offset(self, request):
        try:
            return self.positive_int(
                request.query_params[self.offset_query_param],
            )
        except ValueError as e:
            raise e
        except KeyError:
            return 0

    def positive_int(self, integer_string, cutoff=None):
        try:
            ret = int(integer_string)
        except ValueError as e:
            raise e
        if ret <= 0:
            raise ValueError()
        if cutoff:
            return min(ret, cutoff)
        return ret
