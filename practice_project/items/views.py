from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import ItemsForm, SearchForm
from .models import Items
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
  return render(request, 'items/index.html')

def register(request):
  if (request.method == 'POST'):
    obj = Items()
    item = ItemsForm(request.POST, instance=obj)
    item.save()
    return redirect(to="/items")
  params = {
    'form': ItemsForm()
  }
  return render(request, 'items/register.html', params)

def edit(request, num):
  obj = Items.objects.get(id=num)
  if (request.method == 'POST'):
    item = ItemsForm(request.POST, instance=obj)
    item.save()
    return redirect(to="/items")
  params={
    'id' : num,
    'form' : ItemsForm(instance=obj)
  }
  return render(request, 'items/edit.html', params)

def delete(request, num):
  obj = Items.objects.get(id=num)
  if (request.method == 'POST'):
    obj.delete()
    return redirect(to="/items")
  params={
    'id' : num,
    'object' : obj
  }
  return render(request, 'items/delete.html', params)

class ItemsList(ListView):
  model = Items
  context_object_name = 'items'

  def get_queryset(self):
      queryset = super().get_queryset()
      form = SearchForm(self.request.GET)
      if form.is_valid():
          query = form.cleaned_data.get('query')
          if query is not None:
              queryset = queryset.filter(id=query)
      return queryset

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['search_form'] = SearchForm()
      return context

class ItemsDetail(DetailView):
  model = Items
