from django.contrib import admin
from .models import Service, AdditionalService,  Domain, Language, Profile, WorkExperience, DaySchedule

admin.site.register(Service)
admin.site.register(AdditionalService)
# admin.site.register(Price)
admin.site.register(Domain)
admin.site.register(Language)
# admin.site.register(NannyDomain)
admin.site.register(Profile)
admin.site.register(WorkExperience)
admin.site.register(DaySchedule)
# admin.site.register(Nanny)