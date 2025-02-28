from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.common.filters import IsOwnerFilterBackend
from apps.common.models import MainConfiguration, Country
from apps.common.serilizers import MainConfigurationSerializer, CountryListSerializer


# Create your views here.


class MainConfigurationAPIView(RetrieveAPIView):
    serializer_class = MainConfigurationSerializer

    def get_object(self):
        return MainConfiguration.get_solo()


class CountryListAPIView(ListAPIView):
    serializer_class = CountryListSerializer
    queryset = Country.objects.all()
    pagination_class = None
    filter_backends = [SearchFilter, OrderingFilter, IsOwnerFilterBackend]
    search_fields = ['name', 'ico_code']
    ordering_fields = ['name','ico_code']
