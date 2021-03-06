from __future__ import unicode_literals
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.conf.urls import include, url
#from django.core.urlresolvers import reverse
#from django.urls import reverse
# Create your models here.

#cuisine model
class Cuisine(models.Model):
    cuisineType = models.CharField(choices=( 
        ('African','African'),
        ('American','American'),
        ('Australian','Australian'),
        ('British','British'),
        ('Caribbean','Caribbean'),
        ('Chinese','Chinese'),
        ('French','French'),
        ('Greek','Greek'),
        ('Indian','Indian'),
        ('Italian','Italian'),
        ('Japanese','Japanese'),
        ('Mediterranean','Mediterranean'),
        ('Moroccan','Moroccan'),
        ('Spanish','Spanish'),
        ('Thai','Thai'),
        ('Turkish','Turkish'),
        ('Vietnamese','Vietnamese'),
        ('Unknown','Unknown'),
        ),
        max_length=20,
        default='None',
    )
    def __str__(self):
        return self.cuisineType
        
    #def get_absolute_url(self):
     #   return reverse('cuisine_detail', args=[str(self.id)])
    

#meal model
class Meal(models.Model):
    mealType = models.CharField(choices= (
        ('Breakfast','Breakfast'),
        ('Lunch','Lunch'),
        ('Dinner','Dinner'),
        ('Starter','Starter'),
        ('Dessert','Dessert'),
        ),
        max_length=20,
        default='None',

        )
    cuisineType = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.mealType+' '+self.cuisineType
        
    #def get_absolute_url(self):
     #   return reverse('meal_detail', args=[str(self.id)])

#recipe model
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    serves = models.IntegerField()
    prep_time = models.DurationField((u"Preparation Time"), blank=True)
    cook_time = models.DurationField((u"Cooking Time"), blank=True)
    ingredients = models.TextField(max_length=1500)
    instructions = models.TextField(max_length=15000)
    suits = models.CharField(max_length=1500)
    calories = models.DecimalField(max_digits=5, decimal_places=2, default="")
    fat = models.DecimalField(max_digits=5, decimal_places=2, default="")
    saturates = models.DecimalField(max_digits=5, decimal_places=2, default="")
    carbs = models.DecimalField(max_digits=5, decimal_places=2, default="")
    sugars = models.DecimalField(max_digits=5, decimal_places=2, default="")
    fibre = models.DecimalField(max_digits=5, decimal_places=2, default="")
    protein = models.DecimalField(max_digits=5, decimal_places=2, default="")
    salt = models.DecimalField(max_digits=5, decimal_places=2, default="")
    created_date = models.DateField((u"Date Created"), blank=True)
    published_date  = models.DateField((u"Date Published"), blank=True)
    uploaded_date = models.DateField((u"Date Uploaded"), blank=True)
    warnings =(
        ('May Contain Nuts'),
        ('May Contain Pork/ Meat'),
        )
    mealType = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    cuisineType = models.ForeignKey(Cuisine, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
         return self.name
    
    #def get_absolute_url(self):
     #   return reverse('recipe_detail', args=[str(self.id)])

#utensils model
class Utensil(models.Model):
    name = models.CharField(max_length=200)
    recipeType = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
         return self.name
    
    #def get_absolute_url(self):
     #   return reverse('utensil_detail', args=[str(self.id)])

#source model
class Source (models.Model):
    fname = models.CharField(max_length=25, blank=True), 
    lname = models.CharField(max_length=50, blank=True),
    sourceName = models.CharField(max_length=200, blank=True),
    profession = models.CharField(max_length=25, blank=True),
    recipeType = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    cuisineType = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    
    def __str__(self):
         return self.fname +' '+self.lname+' '+self.sourceName+' '+self.profession
    
    #def get_absolute_url(self):
     #   return reverse('source_detail', args=[str(self.id)])
        
#class Meta:
 #   verbose_name = 'university'
  #  verbose_name_plural = 'universities'