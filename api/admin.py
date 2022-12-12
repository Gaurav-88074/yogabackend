from django.contrib import admin
from .models import Person
from .models import Batch
from .models import BatchesInfo

admin.site.register(Person)
admin.site.register(Batch)
admin.site.register(BatchesInfo)
# Register your models here.
