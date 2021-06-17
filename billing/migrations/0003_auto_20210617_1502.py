# Generated by Django 3.2.4 on 2021-06-17 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_password'),
        ('articles', '0002_alter_article_code'),
        ('billing', '0002_auto_20210617_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Nombre de usuario'),
        ),
        migrations.AlterField(
            model_name='billingbody',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Artículo'),
        ),
        migrations.AlterField(
            model_name='billingbody',
            name='bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.bill', verbose_name='Factura'),
        ),
    ]
