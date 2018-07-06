from django.db import models


# Create your models here.
class Potential(models.Model):
    """docstring for Potential."""

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

    project_type = models.CharField(max_length=255, choices=PROJECT_TYPE_CHOICES)
    project_desc = models.TextField()

    contact_email = models.EmailField()
    contact_name = models.CharField(max_length=255)
    contact_company = models.CharField(max_length=255)
    contact_desc = models.TextField()
