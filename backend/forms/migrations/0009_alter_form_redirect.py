# Generated by Django 3.2 on 2021-06-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_alter_form_redirect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='redirect',
            field=models.CharField(default='pre_events/consult_events', max_length=256),
        ),
    ]
