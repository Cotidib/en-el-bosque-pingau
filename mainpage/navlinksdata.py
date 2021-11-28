from django.http import JsonResponse

# https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html
# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

def getnavlinksdata(request):
    data = [
        {
            'page': 'Proyecto Ingau',
            'links': ['Qué es', 'Los proyectos','Sobre nosotros'],
        },
        {
            'page': 'Cortometraje',
            'links': ['En el Bosque','Sinopsis','Trailer','Detrás de escenas'],
        },
        {
            'page': 'Instalación',
            'links': ['Qué es', 'Reservas'],
        },
    ]
    return JsonResponse(data)