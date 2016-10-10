# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context
from data.models import City


def home(request):
    template = Template(
        """Hello, world! Here are all the data:
{% for city in cities %}{{city.name}}{% endfor %}"""
    )

    cities = City.objects.all()
    context = Context({"cities": cities})

    return HttpResponse(template.render(context))
