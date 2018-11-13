from pathlib import Path

from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    tag = models.CharField(max_length=50, primary_key=True)


class Language(models.Model):
    species = models.CharField(max_length=50, primary_key=True)


class Game(models.Model):
    checksum = models.BinaryField(max_length=2096)
    file_location = models.FilePathField(path=str(Path(__file__).resolve().parent))
    image_location = models.FilePathField(path=str(Path(__file__).resolve().parent), null=True)
    download_url = models.URLField()
    executable = models.CharField(max_length=50)
    year = models.DateField(null=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    tags = models.ManyToManyField(Tag, related_name='used_in')

    def save(self, *args, **kwargs):
        priority = ('english', 'traditional_chinese', 'simplified_chinese')
        rank = sorted([(priority.index(name.language.species), name.name)
                       for name in self.names if name.language.species in priority],
                      key=lambda n: n[0])
        name = rank[0][1]

        self.slug = slugify(name)
        super(Game, self).save(*args, **kwargs)


class Name(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='used_in')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='names')
