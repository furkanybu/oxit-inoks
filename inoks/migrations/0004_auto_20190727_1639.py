# Generated by Django 2.2.1 on 2019-07-27 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inoks', '0003_refund'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refund',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inoks.Product', verbose_name='Ürün Adı'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inoks.Profile', verbose_name='Üye Adı'),
        ),
    ]
