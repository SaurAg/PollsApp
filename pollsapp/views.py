from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.shortcuts import render, get_object_or_404

def index(request):
    all_questions = Question.objects.all()
    return render(request, 'pollsapp/index.html', {'all_questions' : all_questions})

def qsns(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    context = {
        'q' : q,
        }
    return render(request, 'pollsapp/qsns.html', context)

def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        chosen = q.choice_set.get(pk=request.POST["choice"])
    except:
        return render(request, "pollsapp/qsns.html", {'q' : q, 'error_msg' : "Please select a choice to vote"})
    else:
        chosen.votes+=1
        chosen.save()

        return render(request, 'pollsapp/result.html', {'q' : q })

def result(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "pollsapp/result.html", { 'q' : q })