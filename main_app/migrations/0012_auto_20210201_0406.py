# Generated by Django 3.1.5 on 2021-02-01 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_achat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='date_livr_commande',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
