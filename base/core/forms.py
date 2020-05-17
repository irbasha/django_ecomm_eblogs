from django import forms
from martor.fields import MartorFormField

class CommentForm(forms.Form):
	author = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Name',
	}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Email',
	}))
	body = forms.CharField(max_length=200, required=True, widget=forms.Textarea(attrs={
		"rows": "5",
		"class": "form-control",
		"id": "message",
		"placeholder": "Message"
	}))


class ContactForm(forms.Form):
	name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Name',
	}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Email',
	}))
	subject = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Subject',
	}))
	message = forms.CharField(max_length=200, required=True, widget=forms.Textarea(attrs={
		"rows": "10",
		"class": "form-control",
		"id": "message",
		"placeholder": "Message"
	}))

