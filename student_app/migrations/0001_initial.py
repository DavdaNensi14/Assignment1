# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=10, choices=[(b'one', b'1'), (b'two', b'2'), (b'three', b'3'), (b'four', b'4'), (b'five', b'5')])),
                ('email', models.EmailField(max_length=75)),
                ('contact_no', models.IntegerField()),
                ('website', models.TextField(null=True, blank=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('residence_address', models.TextField(null=True, blank=True)),
                ('standard', models.CharField(max_length=50, choices=[(b'five', b'5'), (b'six', b'6'), (b'seven', b'7'), (b'eight', b'8'), (b'nine', b'9'), (b'ten', b'10')])),
                ('roll_no', models.IntegerField()),
                ('fees', models.DecimalField(max_digits=10, decimal_places=3)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(null=True, blank=True)),
                ('School', models.ForeignKey(to='student_app.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
