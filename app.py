import requests
import jinja2
import http.server
import socketserver

# Check API to get answer
query = requests.get("https://mercuryretrogradeapi.com")
data = query.json()['is_retrograde']
# Transform values to be user facing
if data == True:
    answer = 'YES'
if data == False:
    answer = 'NO'

# Print question and answer to console
print('Is Mercury currently in retrograde?')
print(answer)

# Write answer to .html file through Jinja template
outputfile = 'website.html'
subs = jinja2.Environment( 
    loader=jinja2.FileSystemLoader('./')      
    ).get_template('template.html').render(answer=answer)
with open(outputfile,"w") as f: f.write(subs)

# Starts web server to view website at localhost:3000
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/website.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 3000
handler_object = MyHttpRequestHandler
my_server = socketserver.TCPServer(("", PORT), handler_object)
my_server.serve_forever()
