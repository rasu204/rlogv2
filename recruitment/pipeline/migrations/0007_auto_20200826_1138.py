# Generated by Django 3.1 on 2020-08-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0006_auto_20200826_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipeline_class',
            name='Recruiter',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
