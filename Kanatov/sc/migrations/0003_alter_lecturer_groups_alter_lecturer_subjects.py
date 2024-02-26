# Generated by Django 5.0.2 on 2024-02-26 17:57

import sortedm2m.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sc', '0002_remove_lecturer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='groups',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='sc.group', verbose_name='Группы'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='subjects',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='sc.subject', verbose_name='Предметы'),
        ),
    ]