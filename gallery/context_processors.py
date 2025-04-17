from .models import Contact

def contact_links(request):
    return {'contacts': Contact.objects.all()}
