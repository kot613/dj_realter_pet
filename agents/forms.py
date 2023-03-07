from django import forms

from .models import MessageAgent


class MessageForm(forms.ModelForm):
    """ Form for messages to agents """
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg form-control-a',
        'placeholder': 'Name *'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg form-control-a',
        'placeholder': 'Email *'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Comment *',
        'cols': '45',
        'rows': '8'
    }))

    class Meta:
        model = MessageAgent
        fields = ('name', 'email', 'comment')
