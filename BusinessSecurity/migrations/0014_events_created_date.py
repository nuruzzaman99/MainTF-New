# Generated by Django 3.2.7 on 2022-01-07 06:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0013_alter_notification_category_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
