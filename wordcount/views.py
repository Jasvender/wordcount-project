from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordcount = fulltext.split()

    worddictionaries = {}

    for word in wordcount:
        if word in worddictionaries:
            #increase
            worddictionaries[word] +=1
        else:
            #add to the Dictionaries
            worddictionaries[word] = 1
    sortedword = sorted(worddictionaries.items(), key=operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordcount), 'sortedword': sortedword})
