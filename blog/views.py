# Allows us to display templates instead of just dispatching simple messages/responses
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category, Page
from blog.forms import CategoryForm, PageForm

# View = system for processing requests with a web templating system 
# Each view exists within the file as a series of individual functions
# Each view takes in at least one argument -- an HttpRequest object

# Initial view
def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	context_dict = {
		'categories': category_list,
		'pages': page_list,
		'name': "Stanley Kwong"
	}

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	return render(request, 'blog/index.html', context_dict)

def about(request):
	return HttpResponse("The about page<br/><a href='/blog/'>Home</a>")

def category(request, category_name_slug):
	context_dict = {}
	
	try:
		# Can we find a category name slug with the given name?
		# If we can't, the .get() method raises a DoesNotExist exception.
		# So the .get() method returns one model instance or raises an exception.
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name

		# Retrieve all of the associated pages.
		# Note that filter returns >= 1 model instance.
		pages = Page.objects.filter(category=category)

		# Adds our results list to the template context under name pages.
		context_dict['pages'] = pages
		# We also add the category object from the database to the context dictionary.
		# We'll use this in the template to verify that the category exists.
		context_dict['category'] = category
		context_dict['category_slug'] = category_name_slug
	except Category.DoesNotExist:
		pass
	return render(request, 'blog/category.html', context_dict)

def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)
	else:
		form = CategoryForm()

	return render(request, 'blog/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                return category(request, category_name_slug)
        else:
            print(form.errors)
    else:
        form = PageForm()

    context_dict = {'form':form, 'category': cat}

    return render(request, 'blog/add_page.html', context_dict)

