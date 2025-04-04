from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .forms import QuoteRequestForm

class RequestQuoteView(View):
    def get(self, request):
        form = QuoteRequestForm()
        return render(request, 'quote/quote_request.html', {'form': form})

    def post(self, request):
        if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
            return JsonResponse({'error': 'Invalid request'}, status=400)
        
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Request submitted successfully!'})
        return JsonResponse({'errors': form.errors}, status=400)
