# Generated by Django 3.2 on 2021-06-09 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_auto_20210609_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='redirect',
            field=models.CharField(default='#', max_length=256),
        ),
        migrations.AlterField(
            model_name='form',
            name='redirect_delay',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='form',
            name='submit_message',
            field=models.CharField(default='Resposta submetida com sucesso!', max_length=256),
        ),
    ]
