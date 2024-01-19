# Generated by Django 3.2.20 on 2024-01-19 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cohort_name', models.CharField(max_length=150)),
                ('cohort_start', models.DateTimeField(auto_now_add=True)),
                ('cohort_end', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('ranking', models.PositiveIntegerField()),
                ('assignment_completion', models.PositiveIntegerField()),
                ('attendance_average', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nebulaapp.cohort')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_number', models.CharField(max_length=50)),
                ('week_start_date', models.DateField()),
                ('absent_days', models.PositiveIntegerField(default=0)),
                ('present_days', models.PositiveIntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nebulaapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='DailyAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_present', models.CharField(choices=[('absent', 'absent'), ('present', 'present')], default='present', max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='nebulaapp.student')),
            ],
        ),
    ]
