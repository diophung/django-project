from django.forms import ModelForm
from .models import Invitation

class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        fields = '__all__'  # A list of the fields that you want to include in your form


