# Generated by Django 3.0.2 on 2020-04-09 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Content', models.TextField()),
                ('Published', models.DateTimeField(default=datetime.datetime(2020, 4, 9, 4, 17, 56, 427393), verbose_name='date published')),
            ],
        ),
    ]
