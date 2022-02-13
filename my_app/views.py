from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse

# - A single view example
# def sample_view(request):
#     return HttpResponse('Sample Page')

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page',
}

# - dynamic routing with 404 error page handling; set DEBUG=false in settings.py enable 404 page visibility
def news_view(request, topic):
    try:
        return HttpResponse(articles[topic])
    except:
        raise Http404('404 Error')

# - for redirects; e.g. http://127.0.0.1:8000/my_app/0 ---> http://127.0.0.1:8000/my_app/sports
def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]
    return HttpResponseRedirect(reverse('topic-page', args=[topic]))

# - render html template example
def example_view(request):
    return render(request, 'my_app/example.html')

# - using variables with html templates via context
def variable_view(request):
    my_var = {
        'first_name': 'Rosalind', 
        'last_name': 'Franklin',
        'some_list': [1,2,3],
        'some_dict': {
            'inside_key': 'inside_value'
        },
        'user_logged_in': True
    }
    return render(request, 'my_app/variable.html', context=my_var)