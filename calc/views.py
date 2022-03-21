from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator(request):
    c = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c = n1+n2
            elif opr == "-":
                c = n1-n2
            elif opr == "*":
                c = n1*n2
            elif opr == "/":
                c = n1/n2
            elif opr == "%":
                c = n1/n2
                c = c*100

    except:
        c = 'inavalid opr....'
    return render(request,"calculator.html",{'c':c})
