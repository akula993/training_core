from django.urls import path

from training.views import index

urlpatterns = [
path('', index,)
]
