# Generated by Django 3.2.9 on 2024-01-23 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]