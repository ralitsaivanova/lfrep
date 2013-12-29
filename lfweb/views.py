# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import News, Collection, Yarn
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def news(request):
	news_list = News.objects.filter(pub=True).order_by('pub_order')
	paginator = Paginator(news_list, 2) 

	page = request.GET.get('page')
	try:
		news = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		news = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		news = paginator.page(paginator.num_pages)

	return render_to_response("lfweb/news.html",{"news": news},context_instance=RequestContext(request))


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
	collection = Collection.objects.filter(slug = slug)[0]
	
	yarn_list = Yarn.objects.filter(collection=collection,pub=True).order_by('pub_order')
	paginator = Paginator(yarn_list, 6) 

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
														"yarns":yarns,
														"page":page},context_instance=RequestContext(request))