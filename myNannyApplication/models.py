from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AdditionalService(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AgeRange(models.Model):
    range_name = models.CharField(max_length=50)

    def __str__(self):
        return self.range_name

class PetType(models.Model):
    pet_name = models.CharField(max_length=18)

    def __str__(self):
        return self.pet_name

class WorkExperience(models.Model):
    start_year = models.PositiveIntegerField(null=True, blank=True)
    end_year = models.PositiveIntegerField(null=True, blank=True)
    job_place = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.job_place} ({self.start_year}-{self.end_year})"

class DaySchedule(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day = models.CharField(max_length=10, choices=DAY_CHOICES, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField( null=True, blank=True)

    def __str__(self):
        return f"{self.day} ({self.start_time} - {self.end_time})"

class Domain(models.Model):
    name = models.CharField(max_length=100)
    services = models.ManyToManyField(Service) #services_offered
    additional_services = models.ManyToManyField(AdditionalService) #can_help_with
    schedules = models.ManyToManyField(DaySchedule, blank=True)
    work_experiences = models.ManyToManyField(WorkExperience, blank=True)
    age_ranges = models.ManyToManyField(AgeRange, blank=True)
    pet_types = models.ManyToManyField(PetType, blank=True)
    one_time_price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    recurring_price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    domin_about = models.CharField(max_length=300, null=True, blank=True)
    years_of_experience = models.PositiveIntegerField(null=True, blank=True)
    no_of_child = models.PositiveIntegerField(default=0, null=True, blank=True)
    increment = models.PositiveIntegerField(null=True, blank=True)
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, default="Organization")
    organisation_url = models.URLField(null=True, blank=True)
    organisation_name = models.CharField(max_length=100, null=True, blank=True)
    address_proof = models.ImageField(upload_to='verification/address_proof', null=True, blank=True)
    police_certificate = models.ImageField(upload_to='verification/police_certificate', null=True, blank=True)
    driving_license_proof = models.ImageField(upload_to='verification/dlp', null=True, blank=True)
    refrence1_name = models.CharField(max_length=100, null=True, blank=True)
    refrence2_name = models.CharField(max_length=100, null=True, blank=True)
    refrence1_phone = models.CharField(max_length=100, null=True, blank=True)
    refrence2_phone = models.CharField(max_length=100, null=True, blank=True)
    status = models.BooleanField(default=False)
    languages = models.ManyToManyField(Language)
    domains = models.ManyToManyField(Domain, blank=True)

    age = models.PositiveIntegerField(null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    display_name = models.CharField(max_length=150, null=True, blank=True)
    general_about = models.TextField(max_length=400, default=None, null=True, blank=True)
    
    def __str__(self):
        return f"Verification for {self.user.name}"
