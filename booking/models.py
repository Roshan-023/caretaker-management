from django.db import models
from django.contrib.auth import get_user_model
from myNannyApplication.models import Profile

user = get_user_model()

class Booking(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=60, null=True, blank=True)
    day= models.CharField(max_length=15, null=True, blank=True)
    from_time = models.TimeField(null=True, blank=True)
    to_time = models.TimeField(null=True, blank=True)
    is_one_time = models.BooleanField(null=True, blank=True, default=False)
    is_recurring = models.BooleanField(null=True, blank=True, default=False)
    price = models.IntegerField(null=True , blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    district = models.CharField(max_length=20, null=True, blank=True)
    postal_code = models.CharField(max_length=6, null=True, blank=True)
    country = models.CharField(max_length=60, null=True, blank=True)
    other_instructions = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f"{self.user.name} -> {self.profile.user.name} : ({self.from_time} - {self.to_time}) for domain {self.domain_name}"


class RateNanny(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=60, null=True, blank=True)
    content = models.CharField(max_length=60, null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.name} rated {self.profile.user.name} {self.rating}"