from rest_framework.filters import BaseFilterBackend


class IsOwnerFilterBackend(BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """

    def filter_queryset(self, request, queryset, view):
        if request.query_params.get('ico_code'):
            return queryset.filter(ico_code=request.query_params.get('ico_code'))
        return queryset
