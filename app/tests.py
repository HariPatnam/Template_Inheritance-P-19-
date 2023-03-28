from django.test import TestCase

# Create your tests here.

def parent(request):
    return render(request,'parent.html')
