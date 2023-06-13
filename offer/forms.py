from django import forms
from offer.models import Offer


class SearchForm(forms.Form):
    fraze = forms.CharField(
        required=False,
        label="Fraza",
        disabled=False,
        max_length=20,
        min_length=2,
        strip=True,
        empty_value="")


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = [
            "title",
            "price",
            "date_from",
            "date_to",
            "status",
            "category",
            "image",
            "description",]
        widgets = {
            "date_from": forms.DateInput(attrs={
                "type": "date",
                }),
            "date_to": forms.DateInput(attrs={
                "type": "date",
                })}
