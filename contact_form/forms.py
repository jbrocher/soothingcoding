from django.forms import ModelForm, RadioSelect, ChoiceField
from contact_form.models import Potential


class PotentialForm(ModelForm):

    SHOWCASE = 'SC'
    SHOP = 'SP'
    MAINTENANCE = 'MO'
    SEO = 'SEI'
    OTHER = 'U'

    PROJECT_TYPE_CHOICES = (
        (SHOWCASE, 'Site Vitrine'),
        (SHOP, 'E-commerce'),
        (MAINTENANCE, 'Maintenance'),
        (SEO, 'SEO'),
        (OTHER, 'Autre')
    )
    project_type = ChoiceField(choices=PROJECT_TYPE_CHOICES, widget=RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project_desc'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_email'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_company'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_desc'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Potential
        fields = ['project_type', 'project_desc', 'contact_email', 'contact_name', 'contact_desc', 'contact_company']
        widgets = {
            'project_type': RadioSelect()
        }
        empty_label = {'project_type': None}
