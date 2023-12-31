# Generated by Django 4.2.6 on 2023-10-08 17:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=70)),
                ("description1", models.TextField(max_length=1024)),
                (
                    "description2",
                    models.TextField(blank=True, max_length=1024, null=True),
                ),
                (
                    "description3",
                    models.TextField(blank=True, max_length=1024, null=True),
                ),
                (
                    "thumb",
                    imagekit.models.fields.ProcessedImageField(upload_to="albums"),
                ),
                ("tags", models.CharField(max_length=250)),
                ("is_visible", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now_add=True)),
                ("slug", models.SlugField(unique=True)),
                ("lewo", models.BooleanField()),
                ("prawo", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Contakt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Nazwa", models.CharField(blank=True, max_length=70, null=True)),
                ("NIP", models.CharField(blank=True, max_length=70, null=True)),
                ("NrTel", models.CharField(blank=True, max_length=70, null=True)),
                ("EMail", models.CharField(blank=True, max_length=70, null=True)),
                ("Miejscowosc", models.CharField(blank=True, max_length=70, null=True)),
                ("Ulica", models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Factory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titlemain", models.CharField(blank=True, max_length=70, null=True)),
                (
                    "describemain",
                    models.TextField(blank=True, max_length=1024, null=True),
                ),
                ("titlehelp", models.CharField(blank=True, max_length=70, null=True)),
                (
                    "describehelp",
                    models.TextField(blank=True, max_length=1024, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Kwalifikacje",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nazwa", models.CharField(max_length=200)),
                ("opis", models.TextField()),
                ("image", models.ImageField(upload_to="images/")),
                ("lewo", models.BooleanField()),
                ("prawo", models.BooleanField()),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("published_date", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Main",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Wstep", models.CharField(blank=True, max_length=70, null=True)),
                ("Opis", models.TextField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Uslugi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=70, null=True)),
                (
                    "description",
                    models.TextField(blank=True, max_length=1024, null=True),
                ),
                ("photo", models.ImageField(blank=True, null=True, upload_to="albums")),
                ("lewo", models.BooleanField()),
                ("prawo", models.BooleanField()),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("published_date", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="AlbumImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    imagekit.models.fields.ProcessedImageField(upload_to="albums"),
                ),
                (
                    "thumb",
                    imagekit.models.fields.ProcessedImageField(upload_to="albums"),
                ),
                ("alt", models.CharField(default=uuid.uuid4, max_length=255)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("width", models.IntegerField(default=0)),
                ("height", models.IntegerField(default=0)),
                (
                    "slug",
                    models.SlugField(default=uuid.uuid4, editable=False, max_length=70),
                ),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="InstallHome.album",
                    ),
                ),
            ],
        ),
    ]
