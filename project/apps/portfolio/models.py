# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

from filer.fields.image import FilerImageField


@python_2_unicode_compatible
class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    featured_image = FilerImageField()

    the_client = models.TextField(blank=True, null=True)
    the_proposal = models.TextField(blank=True, null=True)
    the_result = models.TextField(blank=True, null=True)

    monthly_visits = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio_single', kwargs={'pk': self.pk})

    def new_visit(self):
        self.monthly_visits = self.monthly_visits + 1
        self.save()
