# Generated by Django 4.1.7 on 2023-03-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='emp_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isApproved', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='employee_tbl',
        ),
    ]
