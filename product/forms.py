from django import forms
from .models import reviews


class productReviewsForm(forms.ModelForm):

    class Meta:
        model = reviews
        fields = ['rate', 'comment',]