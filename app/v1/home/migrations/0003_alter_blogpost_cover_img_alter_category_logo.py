# Generated by Django 4.2.4 on 2023-08-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_category_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='cover_img',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
