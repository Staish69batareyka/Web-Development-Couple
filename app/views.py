from django.http import HttpResponse
from django.shortcuts import render
from .models import HeartRateRecord

def accept_package(request):
    time = request.GET.get('time')
    heart_rate = request.GET.get('rate')

    try: heart_rate = int(heart_rate)
    except(ValueError, TypeError):
        return HttpResponse(
            'Error: Incorrect heart rate recording format',
            status=400)

    if not check_correct_data(time, heart_rate):
        return HttpResponse(
            'Error: Validation or time failure',
            status=400)

    HeartRateRecord.objects.create(time=time, heart_rate=heart_rate)
    message = get_motivation_message(heart_rate)

    response_html = f"""
<div>
    <div>Время: {time}</div>
    <div>Частота сердечных сокращений: {heart_rate} уд/мин.</div>
    <div>'{message}'</div>
</div>
"""
    return HttpResponse(response_html)

def check_correct_data(time: str, rate: int) -> bool:
    if not time or rate is None:
        return False

    elif not (30 <= rate <= 250): # для разумных пределов
        return False
    else:
        last_val = HeartRateRecord.objects.order_by('time').last()
        if last_val and last_val.time >= time :
            return False
        return True

def get_motivation_message(heart_rate: int) -> str:
    if heart_rate >= 100:
        return 'Осторожно что-то не так! Обратитесь к врачу.'
    elif 80 <= heart_rate < 100:
        return 'Осторожно успокойтесь!'
    elif 60 <= heart_rate < 80:
        return 'Хороший результат, Вы движетесь в правильном направлении!'
    else:
        return 'Главное — быть активным!'

