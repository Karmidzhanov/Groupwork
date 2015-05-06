from django.shortcuts import render
from django.views import generic
from django.template import RequestContext, loader
from signup.models import *

from django.http import HttpResponse

def index(request):
    latest_meal_list = Meal.objects.order_by('-date')[:5]
    template = loader.get_template('signup/index.html')
    context = RequestContext(request, {
        'latest_meal_list': latest_meal_list,
    })
    return HttpResponse(template.render(context))
	
class IndexView(generic.ListView):
    template_name = 'signup/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Cadet.objects.all()
		
def detail(request, meal_id):
    try:
        meal = Meal.objects.get(pk=meal_id)
    except Meal.DoesNotExist:
        raise Http404("Meal does not exist")
    return render(request, 'signup/detail.html', {'meal': meal})
