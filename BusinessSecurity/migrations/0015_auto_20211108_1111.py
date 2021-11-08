# Generated by Django 3.2.7 on 2021-11-08 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0014_ticketcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='inputfields',
            name='type',
            field=models.CharField(choices=[('text', 'text'), ('number', 'number'), ('file', 'file'), ('select', 'select')], max_length=264),
        ),
        migrations.CreateModel(
            name='SelectChoiceRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_field', models.ManyToManyField(related_name='selectchoicerelation_selectchoice', to='BusinessSecurity.SelectChoice')),
                ('input_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selectchoicerelation_inputfield', to='BusinessSecurity.inputfields')),
            ],
        ),
    ]