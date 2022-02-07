# Generated by Django 3.2.7 on 2022-02-07 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0054_orderprice_invoice'),
        ('Academy', '0011_coursepackage_max_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorder',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='courseorder',
            name='paypal_email',
        ),
        migrations.RemoveField(
            model_name='courseorder',
            name='paypal_user_name',
        ),
        migrations.RemoveField(
            model_name='courseorder',
            name='update_time',
        ),
        migrations.RemoveField(
            model_name='courseorder',
            name='user',
        ),
        migrations.AddField(
            model_name='courseorder',
            name='business',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='courseorder_business', to='BusinessSecurity.business'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courseorder',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
