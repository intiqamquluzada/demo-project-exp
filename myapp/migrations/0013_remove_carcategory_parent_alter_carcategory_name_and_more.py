# Generated by Django 4.2.6 on 2023-10-20 17:36

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_carcategory_parent_alter_carcategory_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carcategory',
            name='parent',
        ),
        migrations.AlterField(
            model_name='carcategory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Kateqoriya'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='myapp.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]