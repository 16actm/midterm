# Generated by Django 4.2.6 on 2023-10-26 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_firstname', models.CharField(max_length=50)),
                ('p_lastname', models.CharField(max_length=50)),
                ('p_picture', models.ImageField(upload_to='profile_pictures/')),
            ],
        ),
    ]
