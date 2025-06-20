from flask import Flask

app =Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hey Everyone it is Home page</h1>"

@app.route("/about")
def about():
    return "<h1> Hey it is About Page</h1>"

@app.route("/contact")
def contact():
    return "<h1> Hey this is Contact page </h1>"


if __name__ =="__main__":
    app.run(debug=True)