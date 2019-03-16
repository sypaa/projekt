from django.contrib import admin
from .models import Person
from django.urls import reverse
from django.utils.safestring import mark_safe


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'age', 'exp_date')
    list_display = ('first_name', 'last_name', 'age', 'link')
    readonly_fields = ('link',)

    def link(self, obj):
        return mark_safe("<a href='%s'>Download</a>" % (reverse('pdf', args=[obj.id]),))
