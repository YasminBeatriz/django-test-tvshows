# Generated by Django 2.1.7 on 2019-03-29 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tvshows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('1', 'Ongoing'), ('2', 'Finished'), ('3', 'Cancelled')], max_length=2)),
                ('num_episodes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
