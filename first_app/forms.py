from django import forms
from django.core import validators
from first_app.models import Login

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta():
        model = Login
        fields ="__all__"
class FormName(forms.Form):
    def need_start_z(value):
        if value[0].lower()!='z':
            raise forms. ValidationError("Name needs to strat with z")
    name = forms.CharField(validators=[need_start_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please confirm your email")
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required=False,widget = forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        vemail = all_clean_data["verify_email"]
        if email != vemail:
            raise forms.ValidationError("Emails donot match!")
