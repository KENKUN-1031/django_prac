from django.db import models

# Create your models here.
class Items(models.Model):
  itemName = models.CharField(max_length=100)
  itemPrice = models.IntegerField(default=0)
  itemStocks = models.IntegerField(default=0)
  itemCategory = models.CharField(max_length=100)


  def __str__(self):
    return '<Items:id=>' + str(self.id) + ',' + \
      self.itemName + '(' + str(self.itemPrice) + '円)>'
