# Generated by Django 4.2.6 on 2023-10-27 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('famous_womans_app', '0002_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woman',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='famous_womans_app.category'),
        ),
    ]
