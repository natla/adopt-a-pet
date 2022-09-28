# Generated by Django 3.2.15 on 2022-09-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(default='Dog', max_length=30)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('breed', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Boy'), ('F', 'Girl')], max_length=1)),
                ('age', models.IntegerField()),
            ],
        ),
    ]