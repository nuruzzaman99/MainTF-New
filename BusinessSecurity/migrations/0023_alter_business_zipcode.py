# Generated by Django 3.2.7 on 2022-01-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0022_alter_notification_notification_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='zipcode',
            field=models.CharField(max_length=255),
        ),
    ]
