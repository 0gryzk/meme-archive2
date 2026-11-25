from django import forms
from .models import Meme


class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['title', 'year', 'category', 'description', 'image', 'video']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Wolter White'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: 2025'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Откуда взялся мем, контекст и смысл...'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'video': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }