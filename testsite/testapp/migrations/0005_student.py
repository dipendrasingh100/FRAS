# Generated by Django 3.2.18 on 2023-02-26 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_remove_admin_clg_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('enroll', models.CharField(max_length=20)),
            ],
        ),
    ]