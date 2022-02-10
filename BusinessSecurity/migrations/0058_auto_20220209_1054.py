# Generated by Django 3.2.7 on 2022-02-09 04:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0057_auto_20220209_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='nca',
            field=models.FileField(blank=True, help_text='(Supported Format: .pdf)', null=True, upload_to='nca/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='nda',
            field=models.FileField(blank=True, help_text='(Supported Format: .pdf)', null=True, upload_to='nda/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]