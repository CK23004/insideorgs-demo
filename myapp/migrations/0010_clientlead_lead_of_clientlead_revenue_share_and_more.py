# Generated by Django 5.0.3 on 2024-04-27 19:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_userprofile_is_superadmin_alter_image_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='clientlead',
            name='lead_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leads_of', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clientlead',
            name='revenue_share',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='client_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to=settings.AUTH_USER_MODEL),
        ),
    ]
