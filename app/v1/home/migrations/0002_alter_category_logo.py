# Generated by Django 4.2.4 on 2023-08-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='logo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
