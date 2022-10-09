from django.urls import path
from . import views
app_name = "api"

urlpatterns = [
    path('api/GetPizzas', views.api_get_pizza),
]