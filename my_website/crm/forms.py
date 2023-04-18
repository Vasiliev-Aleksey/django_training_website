from django import forms


class OrderForm(forms.Form):
    # required=False - делает заполнение поля необязательным
    name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'css_input'}))
    phone = forms.CharField(max_length=200)
