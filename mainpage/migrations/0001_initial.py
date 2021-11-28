# Generated by Django 3.2.7 on 2021-10-01 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subpage_name', models.CharField(max_length=20)),
                ('subpage_url', models.CharField(max_length=200)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainpage.page')),
            ],
        ),
    ]