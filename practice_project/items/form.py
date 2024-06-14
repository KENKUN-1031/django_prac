from django import forms
from.models import Items

class ItemsForm(forms.ModelForm):
  class Meta:
    model = Items
    fields = ["itemName", "itemPrice", "itemStocks", "itemCategory"]


class SearchForm(forms.Form):
  query = forms.CharField(label="Search by ID", max_length=100)


# class ItemsForm(forms.Form):
#   itemName = forms.CharField(label="itemName")
#   itemPrice = forms.IntegerField(label="itemPrice")
#   itemStocks = forms.IntegerField(label="itemStocks")
#   itemCategory = forms.CharField(label="itemCategory")
