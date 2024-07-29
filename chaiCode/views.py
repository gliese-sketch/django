# from django.http import HTTPResponse
from django.http import HttpResponse

def home(request):
    return HttpResponse('''
<html>
    <head>
        <title>Home Page</title>
    </head>             
    <body>
        <h1>Home Page</h1>
    </body>
</html>
''')

def about(request):
    return HttpResponse('''
<html>
    <head>
        <title>About Page</title>
    </head>             
    <body>
        <h1>About Page</h1>
    </body>
</html>
''')

def contact(request):
    return HttpResponse('''
<html>
    <head>
        <title>Contact Page</title>
    </head>             
    <body>
        <h1>Contact Page</h1>
    </body>
</html>
''')