# Imports
from flask import Flask, render_template
from projects import project_info, project_main

# Initialise app
app = Flask(__name__)


# Add routes
# Home page
@app.route("/")
def home():
    return render_template("index.html", projects=project_info)


# Project information page
@app.route("/project/<string:project_id>")
def open_project(project_id):
    return render_template("project.html", project=project_main[project_id])


# About page
@app.route("/about")
def about_me():
    return render_template("about.html", projects=project_info)


# Run the site
if __name__ == "__main__":
    app.run()
