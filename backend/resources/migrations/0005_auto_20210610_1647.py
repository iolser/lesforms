# Generated by Django 3.2 on 2021-06-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_requestlocation_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationtype',
            name='name',
            field=models.CharField(default='test', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='locationtype',
            name='description',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
