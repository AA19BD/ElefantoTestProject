# Generated by Django 4.1.3 on 2022-11-05 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_book_author_alter_book_favorites_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="core.author",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="favorites",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="book",
            name="genres",
            field=models.ManyToManyField(related_name="books", to="core.genre"),
        ),
        migrations.AlterField(
            model_name="book",
            name="name",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(
                blank=True,
                choices=[
                    ("FANTASY", "FANTASY"),
                    ("DETECTIVES", "DETECTIVES"),
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
    ]
