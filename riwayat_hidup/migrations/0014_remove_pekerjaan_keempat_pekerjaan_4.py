# Generated by Django 4.2.1 on 2023-05-28 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riwayat_hidup', '0013_rename_pekerjaan_2_tahun_pekerjaan_kedua_pekerjaan_tahun_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pekerjaan_keempat',
            name='pekerjaan_4',
        ),
    ]