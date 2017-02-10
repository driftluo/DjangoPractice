from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class':'', 'placeholder':'输入名字'}))
	body = forms.CharField(required=False, widget=forms.Textarea)

	class Meta:
		model = Comment
		fields = ('name', 'body')
