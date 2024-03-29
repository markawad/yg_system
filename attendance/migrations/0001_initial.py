# Generated by Django 3.1.1 on 2021-10-17 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by_card', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StartYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Multiplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sunday_school', models.IntegerField(default=0)),
                ('bible_study', models.IntegerField(default=0)),
                ('summer_club', models.IntegerField(default=0)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='multiplier', to='config.student')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('for_sunday_school', models.BooleanField(default=True)),
                ('for_bible_study', models.BooleanField(default=False)),
                ('attendees', models.ManyToManyField(through='attendance.Attendance', to='config.Student')),
            ],
            options={
                'unique_together': {('date', 'for_sunday_school', 'for_bible_study')},
            },
        ),
        migrations.AddField(
            model_name='attendance',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='attendance.day'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='config.student'),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('student', 'day')},
        ),
    ]
