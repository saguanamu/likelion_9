from django import forms

class GuestbookForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    phonenumber = forms.CharField(label='Phone number', max_length=20)
    content = forms.CharField(label='Say something you want', max_length=100)