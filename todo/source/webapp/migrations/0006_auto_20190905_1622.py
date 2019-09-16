# Generated by Django 2.2.4 on 2019-09-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20190905_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], default='new', max_length=20, verbose_name='Status'),
        ),
    ]
