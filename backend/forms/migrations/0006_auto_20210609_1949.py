# Generated by Django 3.2 on 2021-06-09 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20210609_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='hide_question_numbers',
        ),
        migrations.RemoveField(
            model_name='form',
            name='hide_section_numbers',
        ),
    ]
