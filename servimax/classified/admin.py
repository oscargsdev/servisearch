from django.contrib import admin
from .models import Employer, Worker, Contract, Opinion

class EmployerAdmin(admin.ModelAdmin):
    pass

class WorkerAdmin(admin.ModelAdmin):
    pass

class ContractAdmin(admin.ModelAdmin):
    pass

class OpinionAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Opinion, OpinionAdmin)