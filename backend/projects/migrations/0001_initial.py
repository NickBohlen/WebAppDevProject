# Generated by Django 4.2.16 on 2024-11-03 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
