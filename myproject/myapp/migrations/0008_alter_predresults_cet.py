# Generated by Django 4.0 on 2023-11-13 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_predresults_first_name_predresults_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults',
            name='cet',
            field=models.FloatField(null=True),
        ),
    ]
