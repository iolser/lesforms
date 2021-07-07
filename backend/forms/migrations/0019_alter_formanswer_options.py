# Generated by Django 3.2 on 2021-07-06 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0018_alter_formanswer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formanswer',
            options={'permissions': [('view_own', 'Can view their own form answers'), ('edit_own', 'Can edit own submissions'), ('update_status', 'Can update submission status'), ('request_auth', 'Can request an authentication_key')]},
        ),
    ]
