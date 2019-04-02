# This is a basic python code to start a Web Application using Flask(Hello World)
# Running this code will help to make sure Flask is installed correctly and up for running.


from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return ("Hello World!!!")

@app.route("/about")	
def about():
	return ("This is About Page")
	
@app.route("/contactus")
def contactus():
	return ("<h1>This is Contact Us page</h1>")

@app.route("/blog")	
@app.route("/blog.html")	
def blog():
	return render_template('blog.html')
	
	
if __name__ == '__main__':
	app.run(debug = True)



