# Generated by Django 3.2.18 on 2023-04-18 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0018_classroom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroom',
            old_name='cameraIP',
            new_name='camera_ip',
        ),
        migrations.RenameField(
            model_name='classroom',
            old_name='classID',
            new_name='class_id',
        ),
        migrations.AlterField(
            model_name='classroom',
            name='status',
            field=models.BinaryField(default=0),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('subject', models.CharField(max_length=50)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.classroom')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.teacher')),
            ],
        ),
    ]