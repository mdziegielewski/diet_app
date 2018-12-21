from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .forms import *
from django.views import View
from datetime import date
from random import choice

# Create your views here.


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render (request, "dietapp/login_form.html", {"form":form})

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            return HttpResponse('Błędne dane')

        login(request, user)
        return redirect('/home')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/login')


class HomeView(LoginRequiredMixin,View):

    def get(self,request):
        username = request.user
        return render (request, "dietapp/home.html", {"username":username})




class DetailsView(LoginRequiredMixin, View):


    def get_daily_pfc_fun(self, request):
        user = request.user.id
        person_body = BodyMeasure.objects.get(person_body_id=user)
        person_calories = self.kcalories_calculation(person_body)
        daily_pfc = self.daily_pfc_fun(person_body, person_calories)

        return daily_pfc




    def get(self,request):

        try:
            user = request.user.id
            username = request.user
            person_body = BodyMeasure.objects.get(person_body_id=user)

            person_age = self.age_calculation(person_body)
            person_calories = self.kcalories_calculation(person_body)

            daily_pfc = self.daily_pfc_fun(person_body, person_calories)

            return render(request, "dietapp/details_form.html", {"username": username,
                                                                 "person_body": person_body,
                                                                 "person_age": person_age,
                                                                 "person_calories": person_calories,
                                                                 "daily_pfc": daily_pfc})

        except Exception:
            return redirect ('/bodymeasure')



    def age_calculation(self, person_body):
        person_age = person_body.birth_year
        today = date.today()
        person_age = today.year - person_age
        return person_age



    def kcalories_calculation(self, person_body):
        kcal_calc_weight = person_body.weight
        kcal_calc_height = person_body.height
        kcal_calc_age = self.age_calculation(person_body)
        kcal_calc_gender = person_body.gender
        kcal_calc_body_type = person_body.body_type
        kcal_calc_person_goal = person_body.person_goal
        kcal_calc_physical_activity = person_body.physical_activity


        bmr_fun = self.bmr_calc(kcal_calc_age, kcal_calc_gender, kcal_calc_height, kcal_calc_weight)
        tea_fun = self.tea_calc(kcal_calc_physical_activity)
        epoc_fun = self.epoc_calc(kcal_calc_physical_activity, bmr_fun)
        neat_fun = self.neat_calc(kcal_calc_body_type)

        tdee_fun = round(self.tdee_calc(bmr_fun, epoc_fun, neat_fun, tea_fun))

        return tdee_fun


    def tdee_calc(self, bmr_fun, epoc_fun, neat_fun, tea_fun):
        # TDEE
        TDEE = bmr_fun + tea_fun + epoc_fun + neat_fun
        return TDEE



    def neat_calc(self, kcal_calc_body_type):
        # NEAT
        if kcal_calc_body_type == 1:
            NEAT = 800
            return NEAT
        elif kcal_calc_body_type == 2:
            NEAT = 450
            return NEAT
        elif kcal_calc_body_type == 3:
            NEAT = 300
            return NEAT



    def epoc_calc(self, kcal_calc_physical_activity, bmr_fun):
        # EPOC

        if kcal_calc_physical_activity == 1:
            EPOC = 0
            return EPOC

        elif kcal_calc_physical_activity == 2:
            EPOC = 0.055 * bmr_fun + 20
            return EPOC

        elif kcal_calc_physical_activity == 3:
            EPOC = 0.055 * bmr_fun + 35
            return EPOC

        elif kcal_calc_physical_activity == 4:
            EPOC = 0.055 * bmr_fun + 110
            return EPOC

        else:
            EPOC = 0.055 * bmr_fun + 180
            return EPOC



    def tea_calc(self, kcal_calc_physical_activity):
        # TEA
        if kcal_calc_physical_activity == 1:
            TEA = 0
            return TEA
        elif kcal_calc_physical_activity == 2:
            TEA = 7 * 30 + 7.5 * 10
            return TEA
        elif kcal_calc_physical_activity == 3:
            TEA = 8 * 40 + 8 * 15
            return TEA
        elif kcal_calc_physical_activity == 4:
            TEA = 9 * 60 + 9 * 20
            return TEA
        else:
            TEA = 9 * 90 + 10 * 25
            return TEA



    def bmr_calc(self, kcal_calc_age, kcal_calc_gender, kcal_calc_height, kcal_calc_weight):
        # BMR
        if kcal_calc_gender == 1:  # female
            BMR = (9.99 * kcal_calc_weight) + (6.25 * kcal_calc_height) - (4.92 * kcal_calc_age) - 161
            return BMR
        else:  # male
            BMR = (9.99 * kcal_calc_weight) + (6.25 * kcal_calc_height) - (4.92 * kcal_calc_age) + 5
            return BMR



    def daily_pfc_fun(self, kcal_calc_body_type, tdee_fun):
        if kcal_calc_body_type == 1:
            protein = 0.25 * tdee_fun / 4
            fats = 0.2 * tdee_fun / 9
            carbs = 0.55 * tdee_fun / 4
            return round(protein), round(fats), round(carbs)

        elif kcal_calc_body_type == 2:
            protein = 0.3 * tdee_fun / 4
            fats = 0.15 * tdee_fun / 9
            carbs = 0.55 * tdee_fun / 4
            return round(protein), round(fats), round(carbs)
        else:
            protein = 0.25 * tdee_fun / 4
            fats = 0.25 * tdee_fun / 9
            carbs = 0.5 * tdee_fun / 4
            return round(protein), round(fats), round(carbs)


class RegisterUserView(View):

    def get(self,request):
        form = UserForm()
        return render (request, "dietapp/register_user_form.html", {"form":form})

    def post(self,request):

        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect ('/login')
        else:
            return render(request, "dietapp/register_user_form.html", {"form": form})


class UserUpdate(UpdateView):
    model = BodyMeasure
    fields = ['weight', 'height', 'chest_measure', 'waist_measure', 'hips_measure', 'thigh_measure', 'upper_arm_measure', 'person_goal', 'physical_activity']
    success_url = '/home'



class BodyMeasureView(LoginRequiredMixin, View):

    def get(self,request):

        try:
            user_id = request.user.id
            body_measure = BodyMeasure.objects.get(person_body_id=user_id)
            return HttpResponse("Juz wprowadziles dane")
        except Exception:
            form = BodyMeasureForm()
            return render(request, "dietapp/bodymeasure_form.html", {"form": form})



    def post(self,request):
        form = BodyMeasureForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            birth_year = form.cleaned_data['birth_year']
            gender = form.cleaned_data['gender']
            chest_measure = form.cleaned_data['chest_measure']
            waist_measure = form.cleaned_data['waist_measure']
            hips_measure = form.cleaned_data['hips_measure']
            thigh_measure = form.cleaned_data['thigh_measure']
            upper_arm_measure = form.cleaned_data['upper_arm_measure']
            person_goal = form.cleaned_data['person_goal']
            physical_activity = form.cleaned_data['physical_activity']

            save_person = form.save(commit=False)
            save_person.person_body = request.user
            save_person.save()

            return redirect('/home')
        return render(request, "dietapp/bodymeasure_form.html", {"form": form})



class MealRecipeView(LoginRequiredMixin, View):

    def get(self, request):
        form = MealRecipeForm()
        return render (request, "dietapp/add_recipe_form.html", {"form":form})

    def post(self,request):
        form = MealRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            meal_name = form.cleaned_data['meal_name']
            meal_recipe = form.cleaned_data['meal_recipe']
            meal_preparation_time = form.cleaned_data['meal_preparation_time']
            file = form.cleaned_data['file']
            meal_ingredients = form.cleaned_data['meal_ingredients']

            meal_recipe_object =  MealRecipe.objects.create(meal_name=meal_name, meal_recipe=meal_recipe, meal_preparation_time=meal_preparation_time, file=file)
            meal_recipe_object.meal_ingredients.set(meal_ingredients)
            meal_recipe_object.save()
            return redirect('/home')
        return render(request, "dietapp/add_recipe_form.html", {"form": form})



class DisplayDietView(LoginRequiredMixin, View):


    def random_meal_fun(self):
        meal_recipe_display = MealRecipe.objects.all()
        result= []
        for counter in range(5):
            result.append(choice(meal_recipe_display).meal_name)
        return result


    def get(self,request):


        try:
            username = request.user

            meal_recipe_display = MealRecipe.objects.all()
            detailsView = DetailsView()
            get_daily_pfc = detailsView.get_daily_pfc_fun(request)

            week_meals = []
            for i in range(7):
                week_meals.append(self.random_meal_fun())


            if request.session.get("week_meals") is None:
                request.session["week_meals"] = week_meals
            else:
                week_meals = request.session.get('week_meals')

            return render(request, "dietapp/diet_display_form.html", {"username":username,
                                                                      "get_daily_pfc":get_daily_pfc,
                                                                      "week_meals":week_meals})

        except Exception:
            return redirect('/bodymeasure')

    def post(self, request):

        del request.session['week_meals']
        return redirect('/diet_display')


class AllRecipesView(LoginRequiredMixin, View):


    def get(self, request):
        username = request.user

        meal_recipe_display = MealRecipe.objects.all()
        detailsView = DetailsView()
        get_daily_pfc = detailsView.get_daily_pfc_fun(request)

        meal_recipe = MealRecipe.objects.all()
        meal_ingredients = MealNutrients.objects.all()

        return render (request, "dietapp/all_recipes.html", {"username":username,
                                                             "get_daily_pfc":get_daily_pfc,
                                                             "meal_ingredients":meal_ingredients,
                                                             "meal_recipe":meal_recipe})



class AddIngredientsView(LoginRequiredMixin, View):

    def get(self, request):
        username = request.user
        form = AddIngredientsForm()
        return render (request, "dietapp/add_ingredients_form.html", {"username":username,
                                                                      "form":form})


    def post(self, request):
        username = request.user
        form = AddIngredientsForm(request.POST)
        if form.is_valid():
            nutrients_name = form.cleaned_data['nutrients_name']
            kcal = form.cleaned_data['kcal']
            protein = form.cleaned_data['protein']
            carbohydrates = form.cleaned_data['carbohydrates']
            fats = form.cleaned_data['fats']
            nutrients_group = form.cleaned_data['nutrients_group']
            MealNutrients.objects.create(nutrients_name=nutrients_name, kcal=kcal, protein=protein, carbohydrates=carbohydrates, fats=fats, nutrients_group=nutrients_group)
            return redirect('/home')
        return render(request, "dietapp/add_ingredients_form.html", {"username": username,
                                                                     "form": form})