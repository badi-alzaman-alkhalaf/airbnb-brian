from .models import Info

def footer(request):
    footer = Info.objects.last()
    return {'footer': footer}