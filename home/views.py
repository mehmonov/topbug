import json
import subprocess
from django.shortcuts import render
import difflib

from RestrictedPython import compile_restricted
from RestrictedPython import safe_builtins
from RestrictedPython import utility_builtins
from .models import questions
from django.http import JsonResponse
# Create your views here.
from random import randint
def reset_attempts(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    request.session['attempts'] += 1
    print(request.session['attempts'])
    return JsonResponse({'success': True, 'attempts': request.session['attempts']})

def index(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0

    count = questions.objects.count()
    random_index = randint(0, count - 1)
    q = questions.objects.all()[random_index]
    code = q.code
    question = q.quest
        
    context = {
        'code':code,
        'question':question,
        'attempts': request.session['attempts'],

    }
    print(context)
   
    
    return render(request,'home.html',context)

def compare_code(request):
    result = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code')
        try:
            output = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, text=True)
            result['output'] = output
        except SyntaxError as e:
            result['error'] = f'Syntax error: {e}'
            result['suggestion'] = 'Kodni sintaksisini tekshiring va xatoliklarni to\'g\'rilang'
        except Exception as e:
            result['error'] = f'Error: {e}'
            result['suggestion'] = 'Kodni tekshiring va xatoliklarni to\'g\'rilang'
    return JsonResponse(result)

def qs(request):
    qs = questions.objects.all()
    
    return render(request,'questions.html',{'qs':qs})

def question(request,id):
    q = questions.objects.get(id=id)
    code = q.code
    question = q.quest
    context = {
        'code':code,
        'question':question,
    }
    
    return render(request,'home.html',context)