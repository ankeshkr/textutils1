# Ank created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #with open("1.txt") as f:
     #  a=f.read()
      # return HttpResponse(a)
    #return render(request,'index.html')
    return render(request, "index.html")
def capfirst(request):
    return HttpResponse("cap first")
def analyze(request):
    # get the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')
    charcount=request.POST.get('charcount','off')
    
    print(newlineremove)
    print(djtext)
    analyzed=""
    if removepunc == "on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
        print(analyzed)
        djtext=analyzed
        params = {'purpose':'removed punctuations', 'analyzed_text':analyzed}
        print(params)
        #return render(request,'analyze.html',params)
    if fullcaps== "on":
        analyzed=""
        for char in djtext:
                analyzed=analyzed + char.upper()
        print(analyzed)
        djtext=analyzed
        params = {'purpose':'UPPER CASE', 'analyzed_text':analyzed}
        print(params)
        #return render(request,'analyze.html',params)
    if newlineremove== "on":
        analyzed=""
        for char in djtext:
            if char != '\n' and char !='\r':
                analyzed=analyzed + char
        print(analyzed)
        djtext=analyzed
        params = {'purpose':'New Line Remove', 'analyzed_text':analyzed}
        print(params)
        #return render(request,'analyze.html',params)
    if extraspaceremove== "on":
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed= analyzed+char
        params = {'purpose':'Extraspace Remove', 'analyzed_text':analyzed}
        print(params)
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if charcount== "on":
        count=0
        for char in djtext:
            count=count+1
        count="total characters is " + str(count)
        params = {'purpose':'Character Count', 'analyzed_text':analyzed,'count':count}
        print(params)
        djtext=analyzed
    return render(request,'analyze.html',params)

    if (charcount != 'on' and removepunc != 'on' and extraspaceremove != 'on' and newlineremove != 'on' and fullcaps !='on'):
        return HttpResponse("Error!!")

    #analyze the text
    return HttpResponse("remove punc")
def spaceremove(request):
    return HttpResponse("space remover")
def newlineremove(request):
    return HttpResponse("new line remover")
def charcount(request):
    return HttpResponse("count character")