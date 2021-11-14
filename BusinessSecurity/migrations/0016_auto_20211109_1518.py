# Generated by Django 3.2.7 on 2021-11-09 09:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BusinessSecurity', '0015_auto_20211108_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersbusiness',
            name='user',
        ),
        migrations.AddField(
            model_name='usersbusiness',
            name='user',
            field=models.ManyToManyField(related_name='business_user', to=settings.AUTH_USER_MODEL),
        ),
    ]