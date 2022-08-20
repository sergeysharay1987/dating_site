# Generated by Django 4.0.5 on 2022-07-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_tinder', '0010_alter_customuser_avatar_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1, verbose_name='Gender'),
        ),
    ]