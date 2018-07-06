from django.forms import ModelForm
from contact_form.models import Potential


class PotentialForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['project_desc'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_email'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_company'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_desc'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Potential
        fields = ['project_type', 'project_desc', 'contact_email', 'contact_name', 'contact_desc', 'contact_company']
