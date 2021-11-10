from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# question table 임포트
from polls.models import Question, Choice


# Create your views here.
def index(request):
    # 가장 최근 5개를 가져와서 list에 담기
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    # 변수 dic에 매핑하기
    context = {'latest_question_list': latest_question_list}
    # context 변수를 적용해서 html 텍스트를 만들고, 이를 담아서 HttpResponse 객체를 생성
    # 그리고 반환
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # 조건에 맞는 객체가 없으면 404
    question = get_object_or_404(Question, pk=question_id)
    # 위랑 동일함
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다
        return render(request, 'polls/detail.html',
                      {'question': question, 'error_message': "You didn't select a choice", })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
