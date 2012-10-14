

def search(request):
    location = request.GET.get('location', '')
    query = request.GET.get('query', '')
    filters = request.GET.get('filters', '')

