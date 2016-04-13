# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20160401_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='monthly_visits',
            field=models.IntegerField(default=0),
        ),
    ]
