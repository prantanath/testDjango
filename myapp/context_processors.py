# myapp/context_processors.py

from .forms import add

def add_student_form(request):
    return {'form': add()}
