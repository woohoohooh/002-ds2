# Generated by Django 5.0 on 2024-02-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagrating',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]