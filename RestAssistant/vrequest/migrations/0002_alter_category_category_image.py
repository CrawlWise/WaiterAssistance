# Generated by Django 4.2.7 on 2023-11-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vrequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(upload_to='RestAssistant/vrequest/static/category'),
        ),
    ]