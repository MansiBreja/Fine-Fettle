from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

def validate_bp_low(value):
    if (value<40.0)or(value>140.0):
        raise ValidationError("BP low value should be in range (40-140)")

def validate_bp_high(value):
    if (value<70.0)or(value>250.0):
        raise ValidationError("BP high value should be in range (70-250)")

def validate_rr(value):
    if (value<12.0)or(value>100.0):
        raise ValidationError("Respiratory rate value should be in range (12-100)")

def validate_pr(value):
    if (value<40.0)or(value>120.0):
        raise ValidationError("Pulse rate value should be in range (40-120)")

def validate_temp(value):
    if (value<95.0)or(value>110.0):
        raise ValidationError("Temperature should be in range (95-110)")



class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

    def get_absolute_url(self):
        return reverse("home")

Choice = (
   ('Y', 'Yes'),
   ('N', 'No')
)

class DiagnosisInfo(models.Model):

    Sore_Throat = models.CharField(choices=Choice, max_length=128, null=True,  blank=True);
    Diastolic_Blood_Pressure= models.DecimalField(max_digits=5, decimal_places=2, default="", validators=[
        validate_bp_low
        ]);
    Systolic_Blood_Pressure= models.DecimalField(max_digits=5, decimal_places=2, default="", validators=[
            validate_bp_high
        ]);
    Respiratory_rate = models.DecimalField(max_digits=5, decimal_places=2, default="", validators=[
          validate_rr
        ]);
    Pulse_rate = models.DecimalField(max_digits=5, decimal_places=2, default="", validators=[
         validate_pr
        ]);
    Temperature = models.DecimalField(max_digits=5, decimal_places=2, default="", validators=[
        validate_temp
        ]);

    # def __str__(self):
    #      return self.u_name
    def get_absolute_url(self):
        return reverse("accounts:res")
