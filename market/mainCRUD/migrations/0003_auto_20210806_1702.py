# Generated by Django 3.2.5 on 2021-08-06 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainCRUD', '0002_auto_20210801_0405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='usuario_fecha',
        ),
        migrations.AddField(
            model_name='producto',
            name='prod_descripcion',
            field=models.TextField(default=9.42951438000943e-05, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='prod_imagen',
            field=models.ImageField(default=9.42951438000943e-05, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario_estado',
            field=models.BooleanField(default=True),
        ),
    ]
