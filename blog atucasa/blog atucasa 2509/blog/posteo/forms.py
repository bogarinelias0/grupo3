from django import forms
from posteo.models import Posteo, Comment

class posteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ('__all__')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('content',)