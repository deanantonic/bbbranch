# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolioitem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioitem',
            name='image',
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='the_client',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='the_proposal',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='the_result',
            field=models.TextField(null=True, blank=True),
        ),
    ]
