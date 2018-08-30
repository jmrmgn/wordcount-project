import operator

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def count(request):
    fulltext = request.GET['fulltext']

    word_split = fulltext.split() #this will split the sentence into a list

    word_dict = {}

    for word in word_split:
        if word in word_dict:
            # Increase the count of the word itself
            word_dict[word] += 1
        else:
            # Add the 'new' word into the dictionary
            word_dict[word] = 1

    word_lists = word_dict.items() # converts 'dictionary' into a 'list'

    sorted_words = sorted(word_lists, key=operator.itemgetter(1), reverse=True) # simply reversing the '1' in descending, ex. 5,2,1

    context = {
        "fulltext": fulltext,
        "count": len(word_split),
        "sorted_words": sorted_words,
    }

    return render(request, "count.html", context)
