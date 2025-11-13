from django import forms
from .models import ContactMessage, CommentMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentMessage
        fields = ['name', 'comment']

        
        