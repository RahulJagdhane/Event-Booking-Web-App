# Generated by Django 4.1.1 on 2022-11-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_allevent_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allevent',
            name='event_date',
            field=models.DateField(),
        ),
    ]
