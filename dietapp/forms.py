from django import forms
from .models import *
from django.core.validators import EmailValidator, URLValidator
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='Imię',
                    widget=forms.TextInput(attrs={'placeholder': 'Opcjonalnie'}))
    last_name = forms.CharField(max_length=30, required=False, label='Nazwisko',
                    widget=forms.TextInput(attrs={'placeholder': 'Opcjonalnie'}))
    email = forms.EmailField(max_length=254, label='Email',
                    widget=forms.TextInput(attrs={'placeholder': 'Wymagane'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class BodyMeasureForm(ModelForm):
    class Meta:
        model = BodyMeasure
        exclude = ['person_body']

    def clean(self):
        cleaned_data = super().clean()

        weight = cleaned_data.get("weight")
        height = cleaned_data.get("height")
        birth_year = cleaned_data.get("birth_year")
        chest_measure = cleaned_data.get("chest_measure")
        waist_measure = cleaned_data.get("waist_measure")
        hips_measure = cleaned_data.get("hips_measure")
        thigh_measure = cleaned_data.get("thigh_measure")
        upper_arm_measure = cleaned_data.get("upper_arm_measure")

        if weight < 0:
            msg = "Waga nie może być ujemna"
            self.add_error('weight', msg)

        if height < 0:
            msg = "Na pewno jesteś wyższy"
            self.add_error('height', msg)

        if len(str(birth_year)) != 4:
            msg = "Podaj poprawny rok"
            self.add_error('birth_year', msg)

        if chest_measure < 0:
            msg = "Wartość nie może być ujemna"
            self.add_error('chest_measure', msg)

        if waist_measure < 0:
            msg = "Wartość nie może być ujemna"
            self.add_error('waist_measure', msg)

        if hips_measure < 0:
            msg = "Wartość nie może być ujemna"
            self.add_error('hips_measure', msg)

        if thigh_measure < 0:
            msg = "Wartość nie może być ujemna"
            self.add_error('thigh_measure', msg)

        if upper_arm_measure < 0:
            msg = "Na pewno masz więcej w bicku"
            self.add_error('upper_arm_measure', msg)





class MealRecipeForm(ModelForm):
    class Meta:
        model = MealRecipe
        fields = '__all__'
        widgets = {"meal_ingredients":forms.CheckboxSelectMultiple}


    def clean(self):
        cleaned_data = super().clean()

        meal_preparation_time = cleaned_data.get("meal_preparation_time")
        if meal_preparation_time < 0:
            msg = "Czas nie może być ujemny"
            self.add_error('meal_preparation_time', msg)



class AddIngredientsForm(ModelForm):
    class Meta:
        model = MealNutrients
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        kcal = cleaned_data.get("kcal")
        protein = cleaned_data.get("protein")
        carbohydrates = cleaned_data.get("carbohydrates")
        fats = cleaned_data.get("fats")



        if kcal is not None and kcal < 0:
            msg = "Wartość nie może być ujemna"
            self.add_error('kcal', msg)

        if protein is not None and protein < 0:
            msg = "Wartość nie może być ujemna"
            self.add_error('protein', msg)

        if carbohydrates is not None and carbohydrates < 0:
            msg = "Wartość nie może być ujemna"
            self.add_error('carbohydrates', msg)

        if fats is not None and fats < 0:
            msg = "Wartość nie może być ujemna"
            self.add_error('fats', msg)