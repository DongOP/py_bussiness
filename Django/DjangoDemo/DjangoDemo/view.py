from django.shortcuts import render
 
def hello(request):
    context = {}
    context['test_hello'] = 'Hello MSS!'
    return render(request, 'hello.html', context)