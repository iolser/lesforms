# Generated by Django 3.2 on 2021-06-11 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_auto_20210610_1833'),
        ('forms', '0009_alter_form_redirect'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='forms', to='resources.eventtype'),
        ),
    ]
