from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
# Models = mapper that mediates between data models (Python classes) and a relational database
# Relies on the object-relational mapping (ORM) model

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True) # CharField stores character data, e.g. strings
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "categories"

# One category, multiple pages
class Page(models.Model):
	category = models.ForeignKey(Category) # one-to-many. Creates at least one page using a single Category model
	title = models.CharField(max_length=128, null=False)
	url = models.URLField() # URL Field stores resource URLS
	views = models.IntegerField(default=0) # IntegerField stores integers

	def __str__(self):
		return self.title
