# Generated by Django 4.0.4 on 2022-05-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('school', models.CharField(max_length=150)),
                ('grade', models.IntegerField()),
                ('average_mark', models.DecimalField(decimal_places=1, max_digits=2)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='students_photo')),
            ],
        ),
    ]
