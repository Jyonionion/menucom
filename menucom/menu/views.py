from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Menu

class MenuListView(ListView):
    template_name = 'menu/menu_list.html'
    model = Menu

class MenuDetailView(DetailView):
    template_name = 'menu/menu_detail.html'
    model = Menu