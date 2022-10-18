# Generated by Django 4.1.1 on 2022-10-03 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0002_alter_category_options_alter_category_kind"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("rooms", "0006_alter_amenity_options_alter_room_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="amenities",
            field=models.ManyToManyField(related_name="rooms", to="rooms.amenity"),
        ),
        migrations.AlterField(
            model_name="room",
            name="categories",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rooms",
                to="categories.category",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rooms",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]