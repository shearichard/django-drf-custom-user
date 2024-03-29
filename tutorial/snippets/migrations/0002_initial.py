# Generated by Django 5.0 on 2024-01-14 06:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('snippets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='django_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bar',
            name='barowner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.barowner'),
        ),
    ]
