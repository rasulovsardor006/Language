from django.urls import path

from apps.common.views import CountryListAPIView, MainConfigurationAPIView


urlpatterns = [
    path('MainConfigurationAPIView/', MainConfigurationAPIView.as_view()),
    path('Country/', CountryListAPIView.as_view())
]