from flask import Flask, render_template
import requests
app = Flask(__name__)
# Route for index page
@app.route("/")
def index():
     return render_template("index.html")
# This route gets the user information using the github api
# to display it
@app.route("/githubinfo/<username>")
def get_github_user(username):
    # Url for getting Any valid github user
    url = 'https://api.github.com/users/{}'.format(username)
    # using a with context manager to access the personal token
    # to be use for authentication
    with open("token") as file:
        personal_token = file.read()
    return personal_token
    user_name = "githubname"
    headers = {""}
    data = request.post()
    return "still processing"
if __name__ == "__main__":
    app.run()
