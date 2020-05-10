from django import forms

class CommentForm(forms.Form):
	author = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Name',
		'name': 'name',
	}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Email',
		'name': 'email',
	}))
	body = forms.CharField(max_length=200, required=True, widget=forms.Textarea(attrs={
		"name": "message",
		"rows": "5",
		"class": "form-control",
		"id": "message",
		"placeholder": "Message"
	}))