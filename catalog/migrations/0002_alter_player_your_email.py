# Generated by Django 4.1.1 on 2022-10-11 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='your_email',
            field=models.EmailField(max_length=200),
        ),
    ]
