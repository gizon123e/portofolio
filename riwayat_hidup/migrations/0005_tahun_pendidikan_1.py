# Generated by Django 4.2.1 on 2023-05-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riwayat_hidup', '0004_rename_mymodel_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='tahun_pendidikan_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun_pendidikan_1', models.TextField(default='')),
            ],
        ),
    ]
