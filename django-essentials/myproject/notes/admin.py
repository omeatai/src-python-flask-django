from django.contrib import admin
from . import models
# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated',)
    verbose_name = "Note"
    verbose_name_plural = "Notes"

    # def get_model_name(self):
    #     return "Notes"


admin.site.register(models.Notes, NotesAdmin)
