# Generated by Django 2.2.7 on 2019-11-22 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.CharField(help_text='Squirrel ID', max_length=255, primary_key=True, serialize=False)),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Squirel Age', max_length=20)),
                ('color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='Squirrel Fur Color', max_length=20)),
            ],
        ),
    ]