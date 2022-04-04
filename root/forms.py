from django import forms


class SplitForm(forms.Form):
    string = forms.CharField(label='Ваша строка', required=True)
