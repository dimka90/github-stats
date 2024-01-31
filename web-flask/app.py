from flask import Flask, render_template, request
import requests
app = Flask(__name__)
# Route for index page
@app.route("/")
def index():
     return render_template("index.html")
# This route gets the user information using the github api
# to display it
@app.route("/githubinfo", methods=["POST"])
def get_github_user():
    # Url for getting Any valid github user
    post_name = request.form["username"]
    url = 'https://api.github.com/users/{}'.format(post_name)
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        data = {"Username" : user_data['login'],
                "Name": user_data["name"],
                "Location": user_data["location"],
                "Bio": user_data['bio'],
                "Followers": user_data['followers']
                }
        return  render_template("user_info.html", data = data)
    else:
        return "still processing"
if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
