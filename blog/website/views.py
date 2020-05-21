from django.shortcuts import render


def hello_blog(request):
    listaH = [
        'C',
        'C++',
        'Java',
        'Python',
        'JS',
        'TS',
        'Haskell',
        'Ionic',
        'Django',
    ]
    data = {'name': 'Curso Django',
            'listaHabilidades': listaH, 'coisa': 'COISAAAH'}
    return render(request, 'index.html', data)
