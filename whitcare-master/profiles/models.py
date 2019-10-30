from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Skill(models.Model): 
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField() 

    # from https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17)

    available_weeknights = models.BooleanField()
    available_weekends = models.BooleanField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    skills = models.ManyToManyField(Skill)

    def get_absolute_url(self):
        return reverse('view-profile', args=[self.pk])
    
    def clean(self):
        if not self.available_weeknights and not self.available_weekends:
            raise ValidationError(_("Either weekends or weeknights must be selected."))

