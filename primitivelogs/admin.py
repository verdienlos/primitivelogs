# coding: utf-8

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import PrimitiveLog

# Register your models here.


class PrimitiveLogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PrimitiveLogForm, self).__init__(*args, **kwargs)
        self.fields['eventtxt'].widget = admin.widgets.AdminTextareaWidget()
	self.fields['remark'].widget = admin.widgets.AdminTextareaWidget()


class PrimitiveLogAdmin(admin.ModelAdmin):
    actions = ["send2archive","unarchive"]
    list_filter = ["archived",]
    list_display = ["id","created","eventtxt","archived","remark"]
    search_fields = ["created", "remark",]

    form = PrimitiveLogForm

    def send2archive(self, request, queryset):
        """
        sent log items into archive (let's set archive flag to True)
        """
        for plog in queryset:
            plog.to_archive()
    send2archive.short_description = _("Send to archive")

    def unarchive(self, request, queryset):
        """
        sent log items into archive (let's set archive flag to True)
        """
        for plog in queryset:
            plog.from_archive()
    unarchive.short_description = _("Revert from to archive")


admin.site.register(PrimitiveLog, PrimitiveLogAdmin)


