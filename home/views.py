from django.shortcuts import get_object_or_404, render
from.models import*

# Create your views here.
def cat(request):
     cat=categ.objects.all()
     prodt=products.objects.all()


     return render(request,'indexx.html',{'cr':cat,'pr':prodt,})
def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=products.objects.filter(category=c_page,)
    else:
        prodt=products.objects.all()
    cat=categ.objects.all()
    return render(request,'list.html',{'pr':prodt,'cr':cat})

def proddetails(request,c_slug,product_slug):
    cat=categ.objects.all()
    try:
     prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
         raise e
       
    return render(request,'details.html',{'pr':prod,'cr':cat})

def detail(request):
    cat=categ.objects.all()
    return render(request,'aboutt.html',{'cr':cat})