from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


@permission_required('smartphone.view_smartphone', raise_exception=True)
def home(request):
    return render(request, 'smartphone/home.html')
