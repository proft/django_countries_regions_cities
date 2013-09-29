from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Country(models.Model):
    name = models.CharField('Name', max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'country'
        ordering = ['name']


class Region(models.Model):
    name = models.CharField('Name', max_length=255)
    country = models.ForeignKey(Country, verbose_name='Country')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'region'
        ordering = ['name']


class City(models.Model):
    name = models.CharField('Name', max_length=255)
    country = models.ForeignKey(Country, verbose_name='Country')
    region = models.ForeignKey(Region, verbose_name='Region')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'city'
        ordering = ['name']


class TestModel(models.Model):
    username = models.CharField('Name', max_length=255)
    country = models.ForeignKey(Country, verbose_name='Country')
    region = ChainedForeignKey(Region, chained_field="country", chained_model_field="country", show_all=False, auto_choose=True, verbose_name='Region')
    city = ChainedForeignKey(City, chained_field="region", chained_model_field="region", show_all=False, auto_choose=True, verbose_name='City')

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = 'testmodel'
        ordering = ['username']
