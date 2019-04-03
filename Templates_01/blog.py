# Flask code to run as a web app in which the data is passed to the html.
# Created by Arvind Bahl
# Created on 3/4/2019
#-------------------------------------
from flask import Flask, render_template

app = Flask(__name__)

# Input list which is pass to the html
text1 = [

	{
		'author' : 'Author1',
		'title'  : 'Blog1',
		'content': 'Content1',
		'date'   : 'April 3, 2019' 
	
	},
	
	{
		'author' : 'Author2',
		'title'  : 'Blog2',
		'content': 'Content2',
		'date'   : 'April 4, 2019' 
	
	}
]
# Home page 	
@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", posts = text1, title = "MyHome")

# title of the about page set as a input parameter
@app.route("/about")
def about():
	return render_template("about.html", title = "MyBlog")
	
	
if __name__ == '__main__':
	app.run(debug = True)
	





