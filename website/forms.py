from django import forms
from website.models import Contact


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea,max_length=255)
    subject = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'