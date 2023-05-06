# Generated by Django 3.2.18 on 2023-04-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0027_auto_20230422_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='id',
        ),
        migrations.AddField(
            model_name='camera',
            name='status',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classroom',
            name='room',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
