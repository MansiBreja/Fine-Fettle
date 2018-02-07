from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


class DiagnosisInfo(models.Model):

    # u_name = models.ForeignKey('User');
    bp_low = models.DecimalField(max_digits=5, decimal_places=2, default="");
    bp_high = models.DecimalField(max_digits=5, decimal_places=2, default="");
    resp_rate = models.DecimalField(max_digits=5, decimal_places=2, default="");
    pulse_rate = models.DecimalField(max_digits=5, decimal_places=2, default="");
    temperature = models.DecimalField(max_digits=5, decimal_places=2, default="");
    BMI = models.DecimalField(max_digits=5, decimal_places=2, default="");

    # def __str__(self):
    #      return self.u_name
    def get_absolute_url(self):
        return reverse("accounts:res")
