# Generated by Django 3.2.18 on 2023-04-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0019_alter_student_encoding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='encoding',
            field=models.BinaryField(),
        ),
    ]