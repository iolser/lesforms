# Generated by Django 3.2 on 2021-07-07 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0025_merge_20210707_0327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formanswer',
            options={'permissions': [('update_status', 'Can update submission status'), ('request_auth', 'Can request an authentication_key')]},
        ),
    ]
