from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def count(request):
    words =request.GET["wordtextarea"]
    wordlist = words.split()
    count = len(wordlist)

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    print(worddictionary.items())
    sortedwords = sorted(worddictionary.items(),key = operator.itemgetter(1),reverse= True )
    return render(request,'count.html',{"words":words,"sortedwords": sortedwords ,"count":count})
def about(request):
    return render(request,'about.html')