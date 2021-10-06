from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
# define the page
def home():
    return "Helllo! thisis xXCXCX <h1> the h1 tag <h!>"
    
@app.route("/page")
# define the page
def page():
    return "page! thisis xXCXCX <h1> the page tag <h!>"


# dynamic input/output
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

# redirects to a page (redirect, url_for packages) 
@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))

# render html template (render_template package)
@app.route("/template/<name>")
def template(name):
    # modifies content variables in the html
    return render_template("index.html", content=name, content2=3)

# with lists
@app.route("/list/")
def list():
    # modifies content variables in the html
    return render_template("index.html", content=['Tim', 'Joe', 'Alex'], content2=3)


if __name__ == "__main__":
    app.run()