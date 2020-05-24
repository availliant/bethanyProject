from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FoodSerializer

# List at the end of the views.py
# Lists all customers
class FoodList(APIView):

    def get(self,request):
        foods_json = Food.objects.all()
        serializer = FoodSerializer(foods_json, many=True)
        return Response(serializer.data)



now = timezone.now()
def home(request):
   return render(request, 'crm/home.html',
                 {'crm': home})

@login_required
def food_list(request):
    food = Food.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/food_list.html',
                 {'foods': food})
@login_required
def food_edit(request, pk):
   food = get_object_or_404(Food, pk=pk)
   if request.method == "POST":
       # update
       form = FoodForm(request.POST, instance=food)
       if form.is_valid():
           food = form.save(commit=False)
           food.updated_date = timezone.now()
           food.save()
           food = Food.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/food_list.html',
                         {'foods': food})
   else:
        # edit
       form = FoodForm(instance=food)
   return render(request, 'crm/food_edit.html', {'form': form})

@login_required
def food_delete(request, pk):
   food = get_object_or_404(Food, pk=pk)
   food.delete()
   return redirect('crm:food_list')

@login_required
def food_new(request):
   if request.method == "POST":
       form = FoodForm(request.POST)
       if form.is_valid():
           food = form.save(commit=False)
           food.created_date = timezone.now()
           food.save()
           food = Food.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/food_list.html',
                         {'foods': food})
   else:
       form = FoodForm()
       # print("Else")
   return render(request, 'crm/food_new.html', {'form': form})



@login_required
def entry_list(request):
    entry = Entry.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/entry_list.html',
                 {'entrys': entry})

@login_required
def entry_new(request):
   if request.method == "POST":
       form = EntryForm(request.POST)
       if form.is_valid():
           entry = form.save(commit=False)
           entry.created_date = timezone.now()
           entry.save()
           entry = Entry.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/entry_list.html',
                         {'entrys': entry})
   else:
       form = EntryForm()
       # print("Else")
   return render(request, 'crm/entry_new.html', {'form': form})

@login_required
def entry_edit(request, pk):
   entry = get_object_or_404(Entry, pk=pk)
   if request.method == "POST":
       # update
       form = EntryForm(request.POST, instance=entry)
       if form.is_valid():
           entry = form.save(commit=False)
           entry.updated_date = timezone.now()
           entry.save()
           entry = Entry.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/entry_list.html',
                         {'entrys': entry})
   else:
        # edit
       form = DayForm(instance=entry)
   return render(request, 'crm/entry_edit.html', {'form': form})

@login_required
def entry_delete(request, pk):
   entry = get_object_or_404(Entry, pk=pk)
   entry.delete()
   return redirect('crm:entry_list')

@login_required
def summary(request, pk):
    entry = get_object_or_404(Entry, pk = pk)
    entrys = Entry.objects.filter(entryID = pk)
    foods = Food.objects.filter(entryID = pk)
    sum_fiber = Food.objects.filter(entryID=pk).aggregate(Sum('fiber'))
    sum_vitamin_a = Food.objects.filter(entryID=pk).aggregate(Sum('vitamin_a'))
    sum_vitamin_b6 = Food.objects.filter(entryID=pk).aggregate(Sum('vitamin_b6'))
    sum_vitamin_b9 = Food.objects.filter(entryID=pk).aggregate(Sum('vitamin_b9'))
    sum_vitamin_b12 = Food.objects.filter(entryID=pk).aggregate(Sum('vitamin_b12'))
    sum_vitamin_c = Food.objects.filter(entryID=pk).aggregate(Sum('vitamin_c'))
    sum_vitamin_d = Food.objects.filter(entryID=pk).aggregate(Sum('vitamin_d'))
    sum_vitamin_e = Food.objects.filter(entryID=pk).aggregate(Sum('vitamin_e'))
    sum_calcium = Food.objects.filter(entryID=pk).aggregate(Sum('calcium'))
    sum_omega_3 = Food.objects.filter(entryID=pk).aggregate(Sum('omega_3'))
    sum_weight = Food.objects.filter(entryID=pk).aggregate(Sum('weight'))
    return render(request, 'crm/summary.html', {'entrys': entrys,
                                                    'foods': foods,
                                                    'sum_fiber': sum_fiber,
                                                    'sum_vitamin_a':sum_vitamin_a,
                                                    'sum_vitamin_b6':sum_vitamin_b6,
                                                    'sum_vitamin_b9':sum_vitamin_b9,
                                                    'sum_vitamin_b12':sum_vitamin_b12,
                                                    'sum_vitamin_c':sum_vitamin_c,
                                                    'sum_vitamin_d':sum_vitamin_d,
                                                    'sum_vitamin_e':sum_vitamin_e,
                                                    'sum_calcium':sum_calcium,
                                                    'sum_omega_3':sum_omega_3,
                                                    'sum_weight' :sum_weight,
                                                    })
