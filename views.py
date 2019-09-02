from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def count(request):
    data = request.GET['fulltextarea']
    wordlist = data.split();
    wordlen = len(wordlist)
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedlist= sorted(worddictionary.items(), key = operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':data,'worldlen':wordlen,'worddict':sortedlist})


def contact(request):
    return HttpResponse("<button>click<buton/>")

def about(request):
    return  render(request,'about.html')