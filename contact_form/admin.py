from django.contrib import admin
from contact_form.models import Potential

# Register your models here.


@admin.register(Potential)
class PotentialAdmin(admin.ModelAdmin):
    list_display = ('project_type', 'project_desc', 'contact_name', 'contact_email', 'contact_name', 'contact_company', 'contact_desc', 'dt_contact')
