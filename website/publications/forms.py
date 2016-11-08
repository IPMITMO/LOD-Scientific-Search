from django import forms

class SearchForm(forms.Form):
    text_for_search = forms.CharField(label='What would you want to search?  ', max_length=100)