# Generated by Django 4.0.2 on 2022-05-18 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_tinder', '0003_alter_customuser_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='like',
            field=models.CharField(choices=[('Нравится', 'Нравится'), ('Не_нравится', 'Не нравится')], max_length=100),
        ),
    ]
