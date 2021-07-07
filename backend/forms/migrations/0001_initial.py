# Generated by Django 3.2 on 2021-06-09 17:16

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('color', colorfield.fields.ColorField(default='#DDDDDD', max_length=18)),
            ],
            options={
                'verbose_name_plural': 'Answer statuses',
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('form', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('color', colorfield.fields.ColorField(default='#DDDDDD', max_length=18)),
            ],
            options={
                'db_table': 'formType',
            },
        ),
        migrations.CreateModel(
            name='FormAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answerer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answeredForms', to=settings.AUTH_USER_MODEL)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='editedForms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
