from django.urls import path
from .views import TestView, TestCeleryView


urlpatterns = [
    path('', TestView.as_view(), name='home'),
    path('celery/', TestCeleryView.as_view(), name='celery_page')
]