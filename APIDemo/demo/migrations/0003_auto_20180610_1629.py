# Generated by Django 2.0.6 on 2018-06-10 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20180610_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='head_img',
            field=models.ImageField(blank=True, null=True, upload_to='upload/bdb6f654-4c37-44c4-82dc-e9d3026965f7/', verbose_name='头像'),
        ),
    ]