# Generated by Django 5.1.6 on 2025-03-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tablou',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu', models.CharField(max_length=100)),
                ('imagine', models.ImageField(upload_to='tablouri/')),
            ],
        ),
    ]
