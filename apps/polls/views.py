from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import loader  # need only for function index (type I)
from django.http import Http404  # need only for function detail (type I)

from .models import Question

# def index(request):
#     """Show information without any .html file"""
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)


# def index(request):
#     """(type I) Show information with .html file"""
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


def index(request):
    """(type II) Show information with .html file"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)


# def detail(request, question_id):
#     """(type I) Show information with .html file or Error 404"""
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


def detail(request, question_id):
    """(type II) Show information with .html file or Error 404"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
