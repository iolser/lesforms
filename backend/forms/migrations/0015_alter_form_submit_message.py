# Generated by Django 3.2 on 2021-06-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0014_alter_form_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='submit_message',
            field=models.TextField(default='Resposta submetida com sucesso!'),
        ),
    ]
