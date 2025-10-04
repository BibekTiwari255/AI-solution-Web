from django import forms
from .models import Inquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            "full_name",
            "email",
            "phone",
            "company_name",
            "country",
            "job_title",
            "job_details",
        ]
        widgets = {
            "job_details": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Describe your project requirements, goals, and any specific challenges you're facing..."
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'job_details':
                field.widget.attrs["class"] = "form-textarea"
            else:
                field.widget.attrs["class"] = "form-field"
            field.widget.attrs["placeholder"] = f"Enter your {field_name.replace('_', ' ').title()}"

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "").strip()
        if not phone:
            raise forms.ValidationError("Phone number is required.")
        return phone 