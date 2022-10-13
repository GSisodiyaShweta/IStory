# Generated by Django 4.1.1 on 2022-10-13 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_player_your_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='your_email',
            field=models.EmailField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='your_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]