# Generated by Django 3.2 on 2021-06-09 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_initial'),
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='formfeedbackid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_feedback', to='forms.form'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='formproposalid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_proposal', to='forms.form'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='formsignupid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_signup', to='forms.form'),
        ),
    ]
