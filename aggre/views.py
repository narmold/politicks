from django.http import HttpResponse
from django.shortcuts import render
import json
from pprint import pprint
from eventregistry import *
from datetime import datetime, timedelta 
from aggre.models import posts

 
# def index(request):
#     content = {
#         'title' : 'My First Post',
#         'author' : 'Giles',
#         'date' : '18th September 2011',
#         'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam cursus tempus dui, ut vulputate nisl eleifend eget. Aenean justo felis, dapibus quis vulputate at, porta et dolor. Praesent enim libero, malesuada nec vestibulum vitae, fermentum nec ligula. Etiam eget convallis turpis. Donec non sem justo.',
#     }
#     return render_to_response('index.html', content)

def detail(request, uri):
	return HttpResponse("you're looking at a detail of event: %s", uri)

def index(request):
	#Get Current Date and One day ago
	current = datetime.today()
	current.strftime("%Y-%m-%d")
	d = datetime.today() - timedelta(days=1)
	d.strftime("%Y-%m-%d")

	#Get Events
	er = EventRegistry()
	er.login("narmold@gmail.com","apple1208")
	q = QueryEvents(lang = "eng")
	q.addConcept(er.getConceptUri("Politics", lang = "eng"))   
	q.addLocation(er.getLocationUri("United States"))
	#Sort events by their size of articles
	q.addRequestedResult(RequestEventsInfo(sortBy = "size", count=10))   # return event details for last 10 events
	q.setDateLimit(d, current)
	#q.EventInfoFlags()

	res = er.execQuery(q)

	#   Print all of the info the the execQuery
	pprint(res)

	#Get the amount of events
	event_count = res["events"]["count"] - 1

	#posts.objects.all().delete()

	#Loop through events
	for x in xrange(0, event_count):
		
		post_title = res["events"]["results"][x]["title"]["eng"]
		post_summary = res["events"]["results"][x]["summary"]["eng"]
		post_uri = res["events"]["results"][x]["uri"]
		
		#       Dump the title and summary for each event
		#print(json.dumps(res["events"]["results"][x]["title"]["eng"]))
		#print(json.dumps(res["events"]["results"][x]["summary"]["eng"]))

		post = posts(title = post_title, summary = post_summary)#, uri = post_uri)
		post.save()

	entry_list = list(posts.objects.all())


	#Content to send to index.html (definitely a better way to do this)
	content = {
        'title1' : entry_list[0].title,
        'author1' : 'Giles',
        'date1' : '18th September 2011',
        'body1' : entry_list[0].summary,
        'title2' : entry_list[1].title,
        'author2' : 'Giles',
        'date2' : '18th September 2011',
        'body2' : entry_list[1].summary,
        'title3' : entry_list[2].title,
        'author3' : 'Giles',
        'date3' : '18th September 2011',
        'body3' : entry_list[2].summary,
        # 'title4' : entry_list[3].title,
        # 'author4' : 'Giles',
        # 'date4' : '18th September 2011',
        # 'body4' : entry_list[3].summary,
        # 'title5' : entry_list[4].title,
        # 'author5' : 'Giles',
        # 'date5' : '18th September 2011',
        # 'body5' : entry_list[4].summary,
        # 'title6' : entry_list[5].title,
        # 'author6' : 'Giles',
        # 'date6' : '18th September 2011',
        # 'body6' : entry_list[5].summary,
    }
    	return render(request, 'index.html', content)


	
