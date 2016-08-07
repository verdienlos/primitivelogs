# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.

class PrimitiveLog(models.Model):
    created = models.DateTimeField(_('created'), default=timezone.now)
    eventtxt = models.CharField(_('event text'), max_length=255)
    archived = models.BooleanField(_('is archived'), default=False)
    remark = models.CharField(_('remark'), max_length=255, blank=True)

    class Meta:
        verbose_name = _('Log')
        verbose_name_plural = _('Logs')
	ordering = ['-created']
	permissions = (
            ('moderate_primitivelogs', 'Can moderate primitive logs'),
        )

    def to_archive(self):
	if not self.archived:
	    self.archived=True
	    self.save(update_fields=['archived'])


    def from_archive(self):
	if self.archived:
	    self.archived=False
	    self.save(update_fields=['archived'])


