# Generated by Django 5.0.4 on 2024-05-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
