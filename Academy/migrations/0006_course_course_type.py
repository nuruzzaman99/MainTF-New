# Generated by Django 3.2.7 on 2021-10-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academy', '0005_auto_20211017_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('Business', 'Business'), ('Personal', 'Personal')], default='Business', max_length=264),
            preserve_default=False,
        ),
    ]