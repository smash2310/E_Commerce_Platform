from django import forms



from django.contrib.auth.forms import UserCreationForm

# from Model.models import User, Profile, BillingAddress
_models = __import__("MVC Structure.Model.models")
_models = _models.Model.models
# ****************APP LOGIN****************

class ProfileForm(forms.ModelForm):
    address_1 = forms.CharField(max_length=300,required=False, widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = _models.Profile
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    class Meta:
        model = _models.User
        fields = ('email', 'password1', 'password2')

# ****************APP LOGIN****************
class BillingForm(forms.ModelForm):
    class Meta:
        model = _models.BillingAddress
        fields = ['address', 'zipcode', 'city', 'country']
