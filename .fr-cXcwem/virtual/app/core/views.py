from django.http import HttpResponse
#importando e lendo de django template
from django.template import loader

#our view which is a function named index
def index(request):

    #pegando nosso template
    template = loader.get_template('index.html')

    #renderizando otemplate in HttpResponse
    return HttpResponse(template.render())
