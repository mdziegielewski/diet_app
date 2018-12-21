from django.db import models
from django.contrib.auth.models import User

# Create your models here.



NUTRIENTS_GROUPS_CHOICES = (
    (1, "Owoce i warzywa"),
    (2, "Mięso"),
    (3, "Ryby"),
    (4, "Produkty zbożowe"),
    (5, "Jajka"),
    (6, "Olej"),
)

BODY_TYPE_CHOICES = (
    (1, "ektomorfik"),
    (2, "mezomorfik"),
    (3, "endomorfik"),
)

GOAL_CHOICES = (
    (1, "utrata wagi"),
    (2, "utrzymanie wagi"),
    (3, "przybranie na wadze"),

)

PHYSICAL_ACTIVITY_CHOICES = (
    (1, "Znikoma (brak ćwiczeń, lekka praca)"),
    (2, "Bardzo mała (ćwiczenia raz na tydzień)"),
    (3, "Umiarkowana (ćwiczenia 2-3 razy w tygodniu)"),
    (4, "Duża (trening kilka razy w tygodniu)"),
    (5, "Bardzo duża (trening kilka razy w tygodniu, praca fizyczna)"),

)

GENDER_CHOICES = (
    (1, "female"),
    (2, "male"),
)


class MealNutrients(models.Model):  #per 100 gram

    nutrients_name = models.CharField(max_length=64)
    kcal = models.DecimalField(max_digits=5, decimal_places=1)
    protein = models.DecimalField(max_digits=5, decimal_places=1)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=1)
    fats = models.DecimalField(max_digits=5, decimal_places=1)
    nutrients_group = models.SmallIntegerField(choices=NUTRIENTS_GROUPS_CHOICES, default=False)


    def __str__(self):
        return self.nutrients_name

class MealRecipe(models.Model):

    meal_name = models.CharField(max_length=128)
    meal_recipe = models.TextField()
    meal_preparation_time = models.IntegerField()
    file = models.FileField()

    # meal_ingredients = models.ForeignKey(MealNutrients, on_delete=models.CASCADE, default=False)
    meal_ingredients = models.ManyToManyField(MealNutrients)


    def __str__(self):
        return self.meal_name



class BodyMeasure(models.Model):

    weight = models.SmallIntegerField()
    height = models.SmallIntegerField()
    birth_year = models.SmallIntegerField()
    gender = models.SmallIntegerField(choices=GENDER_CHOICES)
    chest_measure = models.SmallIntegerField()
    waist_measure = models.SmallIntegerField()
    hips_measure = models.SmallIntegerField()
    thigh_measure = models.SmallIntegerField()
    upper_arm_measure = models.SmallIntegerField()
    body_type = models.SmallIntegerField(choices=BODY_TYPE_CHOICES, default=False)
    person_goal = models.SmallIntegerField(choices=GOAL_CHOICES, default=False)
    physical_activity = models.SmallIntegerField(choices=PHYSICAL_ACTIVITY_CHOICES, default=False)

    person_body = models.ForeignKey(User, on_delete=models.CASCADE)












