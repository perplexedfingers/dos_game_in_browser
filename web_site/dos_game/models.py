from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    tag = models.CharField(max_length=50, primary_key=True)


class Language(models.Model):
    species = models.CharField(max_length=50, primary_key=True)


class Game(models.Model):
    checksum = models.BinaryField(max_length=4096)
    file_location = models.CharField(max_length=50)
    image_location = models.CharField(max_length=50, null=True)
    download_url = models.URLField()
    executable = models.CharField(max_length=50)
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
