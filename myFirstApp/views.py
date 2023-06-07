from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, World!")

def form_submission(request):
    if request.method == 'POST':
        # Отримання даних з форми
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')

        # Передача даних в шаблон
        context = {
            'name': name,
            'surname': surname,
            'email': email
        }

        # Повернення шаблону з відображеними даними
        return render(request, 'result.html', context)

    # Якщо метод запиту не POST, повертаємо пусту сторінку
    return render(request, 'form.html')
