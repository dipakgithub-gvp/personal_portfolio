# Generated by Django 2.1.5 on 2020-08-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='portfolio/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
