# Generated by Django 3.2.7 on 2021-11-06 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='users/default.jpg', upload_to='users/'),
        ),
    ]