from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant,Tourspots
# Create your views here.

# def result_rest(request) :
#     input = request.GET['input']
#     # print(input)
#     # context = {'gu':input}
#     res = Restaurant.objects.all()
#     # print(res)
#     restaurant=[]
#     for i in range(len(res)):
#         # print(i)
#         if res[i].category == input:
#             restaurant.append(res[i])
#
#     context = {'gu': restaurant}
#     return render(request, "search_result/result_rest.html",context)

def result_rest(request) :
    lat = request.GET['latitude']
    long = request.GET['longitude']
    context = {
        'latitude' : lat,
        'longitude' : long
    }
    return render(request, "search_result/result_rest.html", {'context': context})


def result_tour(request) :
    return render(request, "search_result/result_tour.html")