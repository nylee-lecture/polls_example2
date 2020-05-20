from django.shortcuts import render
from polls.models import Question, Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context_1 = {'name': latest_question_list}
    return render(request, 'polls/index.html', context_1)
