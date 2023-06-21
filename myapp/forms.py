from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# buat forms
class RespondentForm(UserCreationForm):
    nim = forms.IntegerField()
    class Meta:
        model = User
        fields = [
            "username",
            "nim",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super(RespondentForm, self).save(commit=False)
        user.nim = self.cleaned_data.get("nim")
        if commit:
            user.save()
        return user