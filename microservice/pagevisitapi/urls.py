from django.urls import include, path
from .api.views import PageVisitApiView

urlpatterns = [
    path('', PageVisitApiView.as_view(),name='pagevisit'),
]