# Generated by Django 4.2.1 on 2023-05-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riwayat_hidup', '0009_tahun_pendidikan_satu_sekolah_pendidikan_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='tahun_pendidikan_dua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun_pendidikan_2', models.TextField(default='')),
                ('sekolah_pendidikan_2', models.TextField(default='')),
            ],
        ),
    ]