# Generated by Django 4.0 on 2023-11-23 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_recommendedcourse_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendedcourse',
            name='analysis',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
