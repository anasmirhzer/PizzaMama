from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


# Create your views here.
def index(request):
    # pizzas = Pizza.objects.all()
    # pizzas_infos = [pizza.name +" : " + str(pizza.price) + "$" for pizza in pizzas]
    # pizzas_infos_str = ", ".join(pizzas_infos)
    # return HttpResponse(f"Pizzas : {pizzas_infos_str}")
    pizzas = Pizza.objects.all()
    return render(request, 'menu/index.html', {'pizzas': pizzas})