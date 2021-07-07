# Generated by Django 3.2 on 2021-07-06 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0010_auto_20210629_1713'),
        ('forms', '0019_auto_20210706_0226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start', models.CharField(max_length=128)),
                ('end', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('emergencyContact1', models.CharField(blank=True, max_length=128, null=True)),
                ('emergencyContact2', models.CharField(blank=True, max_length=128, null=True)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='resources.event')),
            ],
        ),
    ]
