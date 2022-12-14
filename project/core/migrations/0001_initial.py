# Generated by Django 4.1.3 on 2022-11-04 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(blank=True, max_length=250, null=True)),
                ("age", models.IntegerField(blank=True, default=0)),
            ],
            options={
                "verbose_name": "Author",
                "verbose_name_plural": "Authors",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(blank=True, max_length=250, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("favorites", models.BooleanField(default=False)),
                ("publish_date", models.DateField(auto_now_add=True)),
                ("average_rating", models.FloatField(blank=True, default=0, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="books",
                        to="core.author",
                    ),
                ),
            ],
            options={
                "verbose_name": "Book",
                "verbose_name_plural": "Books",
                "ordering": ["publish_date"],
            },
        ),
        migrations.CreateModel(
            name="Genre",
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
                    "name",
                    models.CharField(
                        choices=[
                            ("FANTASY", "FANTASY"),
                            ("DETECTIVES ", "DETECTIVES "),
                            ("HORROR", "HORROR"),
                            ("ADVENTURES", "ADVENTURES"),
                            ("POETRY", "POETRY"),
                            ("LOVE_NOVELS", "LOVE_NOVELS"),
                            ("THRILLERS", "THRILLERS"),
                            ("COMICS AND MANGA", "COMICS AND MANGA"),
                            ("PROSE", "PROSE"),
                            ("BUSINESS LITERATURE", "BUSINESS LITERATURE"),
                            ("PSYCHOLOGY", "PSYCHOLOGY"),
                            ("ART AND CULTURE", "ART AND CULTURE"),
                            ("SCIENTIFIC LITERATURE", "SCIENTIFIC LITERATURE"),
                            ("HOBBIES AND LEISURE", "HOBBIES AND LEISURE"),
                            ("LEARNING LANGUAGES", "LEARNING LANGUAGES"),
                            ("STORY", "STORY"),
                            ("COMPUTER LITERATURE", "COMPUTER LITERATURE"),
                            ("BOOKS FOR PRESCHOOLERS", "BOOKS FOR PRESCHOOLERS"),
                            ("CHILDREN'S DETECTIVES", "CHILDREN'S DETECTIVES"),
                            ("CHILDRENS ADVENTURE BOOKS", "CHILDRENS ADVENTURE BOOKS"),
                            ("BOOKS FOR TEENAGERS", "BOOKS FOR TEENAGERS"),
                        ],
                        default="POETRY",
                        max_length=250,
                    ),
                ),
            ],
            options={
                "verbose_name": "Genre",
                "verbose_name_plural": "Genres",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Review",
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
                ("author", models.CharField(blank=True, max_length=250, null=True)),
                ("rating", models.IntegerField(blank=True, default=0)),
                ("review_text", models.TextField(blank=True)),
                (
                    "books",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="core.book",
                    ),
                ),
            ],
            options={
                "verbose_name": "Review",
                "verbose_name_plural": "Reviews",
                "ordering": ["author"],
            },
        ),
        migrations.AddField(
            model_name="book",
            name="genres",
            field=models.ManyToManyField(related_name="books", to="core.genre"),
        ),
    ]
