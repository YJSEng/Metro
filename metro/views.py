from django.shortcuts import render
from .models import Member
from django.http import  HttpResponseRedirect
from django.template import loader
from .forms import ReviewForm
from django.views.generic.edit import FormView, CreateView

from django.views import View
from django.views.generic.base import TemplateView

def starting_page(request):
    mymembers=Member.objects.all().values()
    context={
        'mymembers':mymembers,
    }
    
    return render(request, "metro/index.html",context)


def starting_page1(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }

    return render(request, "metro/showuser.html", context)



def details(request, id):
    mymember = Member.objects.get(id=id)
    context = {
        'mymember': mymember,
    }
    return render(request, "metro/details.html", context)

def topup(request,id):
    mymember = Member.objects.get(id=id)
    context = {
     'mymember': mymember,
     }
   
    return render(request, "metro/topup.html",context)


def travel(request, id):
    mymember = Member.objects.get(id=id)
    context = {
        'mymember': mymember,
    }

    return render(request, "metro/travel.html", context)
    

def updaterecord(request, id):
    mymember = Member.objects.get(id=id)
    
    topup = request.POST['topup']
    context = {
        'topup': topup,
        'mymember':mymember

    }
    if topup=="":
        topup=0
    context = {
        'topup': topup,
        'mymember': mymember

    }

    if int(topup)<100:
        return render(request, "4041.html/", context)
    member = Member.objects.get(id=id)
    member.topup =  int(topup)+member.topup
 
    member.save()
    
    return HttpResponseRedirect("/details/"+str(id))


    
def updaterecord1(request, id):
    mymember = Member.objects.get(id=id)
    context = {
        'mymember': mymember,
    }

    stationtravel = request.POST['stationtravel']
    if int(mymember.topup) < 15:
        return render(request,"404.html/",context)
    member = Member.objects.get(id=id)
    if int(stationtravel)<= 3:

       
        member.topup = member.topup-15*(int(stationtravel))
        context = {
            'topup': member.topup,
            'mymember': mymember

        }

        if int(member.topup) >=0:
            member.save()
            return HttpResponseRedirect("/details/"+str(id))
        else:


            return render(request, "404.html/",context)
        
        
    
    if int(stationtravel) > 3:

        member = Member.objects.get(id=id)
        member.topup = member.topup-5*(int(stationtravel))
        context = {
            'topup': member.topup,
            'mymember': mymember

        }
        if int(member.topup) >= 0:
            member.save()
            return HttpResponseRedirect("/details/"+str(id))
        else:

            return render(request, "404.html/", context)


class ReviewView(View):
    def get(self,request):
        form=ReviewForm()
       # return render(request, "reviees/review.html", {"form": form})
        return render(request, "metro/adduser.html", {"form": form})
    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect("/thankyou")
            return render(request, "metro/index.html", {"form": form})

       # return render(request,"reviees/review.html",{"form":form})
        return render(request, "metro/adduser.html", {"form": form})


# Create your views here.
