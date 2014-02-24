# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import News, Collection, Yarn
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def collections(request):
	collections = Collection.objects.filter(pub=True,parent__isnull = True).order_by('pub_order')
	render_collections = list()
	for c in collections:
		
		render_collections.append({
			'main': c,
			'sub': Collection.objects.filter(pub=True).filter(parent = c).order_by('pub_order')	
			})


	return render_to_response("lfweb/collezioni.html",{"collections": render_collections},context_instance=RequestContext(request))

def detail(request,slug):
	collection = get_object_or_404(Collection,slug = slug) 
	tecnicalcards = collection.tecnicalcard_set.filter(pub=True).order_by('pub_order')

	yarn_list = Yarn.objects.filter(collection=collection,pub=True).order_by('pub_order')
	paginator = Paginator(yarn_list, 8) 

	page = request.GET.get('page')
	try:
		yarns = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		yarns = paginator.page(1)
		page = 1
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		yarns = paginator.page(paginator.num_pages)

	page = int(page)	
	return render_to_response("lfweb/collezioni_det.html",{"collection": collection,
														"tecnicalcards":tecnicalcards,
														"yarns":yarns,
														"page":page},context_instance=RequestContext(request))