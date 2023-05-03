from django import forms


class OrderForm(forms.Form):
    # required=False - делает заполнение поля необязательным
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
