# Generated by Django 3.2 on 2021-07-04 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0017_certificate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formanswer',
            options={'permissions': [('view_own', 'Can view their own Form Answers.'), ('edit_own', 'Can edit own submissions.'), ('update_status', 'Can update submission status.'), ('request_auth', 'Can request an authentication_key.')]},
        ),
    ]
