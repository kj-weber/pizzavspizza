from django.urls import path
from . import views

urlpatterns = [
    path('',views.PizzariaListAPIView.as_view(), name='pizzeria_list')
]