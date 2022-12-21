# Generated by Django 4.1.4 on 2022-12-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=50)),
                ('target_link', models.URLField(blank=True, max_length=300, null=True)),
                ('programmer', models.CharField(max_length=50)),
                ('programmer_link', models.URLField(blank=True, max_length=300, null=True)),
                ('text', models.TextField(max_length=200)),
            ],
        ),
    ]