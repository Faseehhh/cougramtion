# Generated by Django 4.0 on 2023-11-19 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_predresults_strand'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendedcourse',
            name='percentage',
            field=models.FloatField(default=0.0),
        ),
    ]