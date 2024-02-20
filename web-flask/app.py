from flask import Flask, render_template, request, flash
import requests
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Route for index page
@app.route("/")
def index():
    """"
    This function handles the index page

    Return:
          html
    """
    return render_template("index.html")


@app.route("/githubinfo", methods=["POST"])
def get_github_user():
    """
    This function get a particular user
    info on github
    Return:
          html
    """
    post_name = request.form["username"]
    # url for getting a specific github username
    url = 'https://api.github.com/users/{}'.format(post_name)
    try:
        response = requests.get(url)
        # checking if it was a success
        if response.status_code == 200:
            #converting it to python objects
            user_data = response.json()
               
            #extracting each user image
            avatar_url =  user_data.get('avatar_url', '')
            # Extracting the return values from the api and storing in a dictionary
            data = {"username" : user_data['login'],
                    "Name": user_data["name"],
                    "Location": user_data["location"],
                    "Bio": user_data['bio'],
                    "Followers": user_data['followers'],
                    }
            return  render_template("user_info.html", data = data, avatar_url = avatar_url)
        else:
            flash("{} oops, is not on Github".format(post_name))
            return render_template("index.html")

    except requests.exceptions.RequestException as e:
        flash("You are offline")
        return render_template("index.html")
  


@app.route("/get_user_projects", methods =["GET"])
def get_user_projects():
    """
    This function make a requests to the github api
    for a particular github user

    Return: 
          (htmL) - githu user profile
    """
    username = request.args.get("username")
    # obtainning access token
    with open("token") as file:
        # Reading  personal access token to add to headers
        token = file.read().strip()
    base_url = f'https://api.github.com/users/{username}/repos'
    headers  = {'Authorization': 'token {}'.format(token)}
    response = requests.get(base_url, headers=headers)
    # checking if it was a success
    if response.status_code == 200:
        projects = response.json()

        return render_template("projects.html", projects = projects)
    else:
        return "Still processing"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
