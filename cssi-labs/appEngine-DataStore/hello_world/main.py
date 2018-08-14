# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import jinja2
import os
from google.appengine.ext import ndb

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Cssipage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>Goodbey, World!</h1>')



class MainPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        query_result = Blog.query().order(Blog.firstname)

        template_dic = {"country": "usa",
                       "region_name": "north east",
                       "region_num": 121,
                       "url": "https://generocity.org/philly/wp-content/uploads/sites/2/2017/05/Summer.-Photo-via-Flickr-user-Peter-Miller-used-under-a-Creative-Commons-license.jpg",
                       "city": ["new york","boston", "philadelphia"],
	                   "message": "welcome to: ",
                       "query_result": query_result
                       }


        self.response.write(welcome_template.render(template_dic))


class ShowMemeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("hello from ShowMemeHandler")
    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        firstname = self.request.get('alsofirstname')
        lastname = self.request.get('lastname')
        age = self.request.get('age')

        entity = Blog(firstname = firstname, lastname = lastname)
        entity.put()

        webform_dict = {"fn": firstname, "ln": lastname, "ae": age}
        self.response.write(results_template.render(webform_dict))
        # self.response.write(firstname)

class Blog(ndb.Model):
    firstname = ndb.StringProperty()
    lastname = ndb.StringProperty()
    created_at = ndb.DateTimeProperty(auto_now_add = True)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/showresults', ShowMemeHandler),
    ('/cssi', Cssipage)],
    debug=True)
