from django import forms

from tpaga_project_1.models import Item


class ItemForm(forms.Form):
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), label="Select one or many items")
    order_description = forms.CharField(label="Order description")
