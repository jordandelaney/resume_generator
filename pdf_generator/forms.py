from django import forms

class ResumeForm(forms.Form):
    name = forms.CharField(label="Your name")
