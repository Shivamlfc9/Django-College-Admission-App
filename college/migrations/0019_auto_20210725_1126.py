# Generated by Django 3.1.7 on 2021-07-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0018_auto_20210720_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='message',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='course',
            field=models.CharField(choices=[('Computer Science Engineering', 'Computer Science Engineering'), ('Information Technology Engineering', 'Information Technology Engineering'), ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'), ('Electronics Engineering', 'Electronics Engineering')], max_length=100),
        ),
    ]
