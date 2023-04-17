from django import forms

from .models import MenuItem


class MenuItemsForm(forms.ModelForm):
    name = forms.CharField()
    url = forms.CharField()

    class Meta:
        model = MenuItem
        fields = "__all__"
