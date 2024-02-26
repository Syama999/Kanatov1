# Generated by Django 5.0.2 on 2024-02-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sc', '0003_alter_lecturer_groups_alter_lecturer_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='groups',
            field=models.ManyToManyField(blank=True, to='sc.group', verbose_name='Группы'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='sc.subject', verbose_name='Предметы'),
        ),
    ]