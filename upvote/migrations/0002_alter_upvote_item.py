# Generated by Django 5.1.5 on 2025-07-09 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmapItems', '0001_initial'),
        ('upvote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upvote',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_upvotes', to='roadmapItems.roadmapitem'),
        ),
    ]
