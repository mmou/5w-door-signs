
import requests
people = []
search_url = "http://web.mit.edu/bin/cgicso?options=general&query="

for person in people:
	url = search_url + "+".join(person.split())
	r = requests.get(url)
	start = r.text.find("<PRE>")
	end = r.text.find("</PRE>")
	print r.text[start:end]
	print "\n"