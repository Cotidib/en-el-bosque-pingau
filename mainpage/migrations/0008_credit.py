# Generated by Django 3.2.7 on 2021-10-31 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_alter_image_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=200)),
                ('person_role', models.CharField(max_length=200)),
                ('person_area', models.CharField(max_length=200)),
            ],
        ),
    ]
