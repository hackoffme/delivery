# Generated by Django 4.1.1 on 2022-11-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerstg',
            name='tg_id',
            field=models.IntegerField(db_index=True, unique=True, verbose_name='ID пользователя telegram'),
        ),
    ]
