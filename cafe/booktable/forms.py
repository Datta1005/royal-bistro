from django import forms
from .models import BookTableModel

class BookTableForm(forms.ModelForm):
    class Meta:
        model = BookTableModel
        fields = '__all__'