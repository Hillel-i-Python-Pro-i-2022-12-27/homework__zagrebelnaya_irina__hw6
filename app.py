from flask import Flask, render_template
from application.body.usersgenerator import print_result_of_generation_users
from application.body.requesttoapi import get_astronaut_from_json
from application.body.actions_with_files import return_data_from_csv_average_function, to_create_file, to_read_file
import asyncio

app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return "Hello!"


@app.route("/generate-users/")
def generate_users():  # put application's code here
    users = print_result_of_generation_users(number=5)
    return render_template("users.html", users=users)


@app.route("/space/")
def space():  # put application's code here
    astronauts = asyncio.run(get_astronaut_from_json())
    return render_template("space.html", astronauts=astronauts)


@app.route("/mean/")
def mean():  # put application's code here
    average = return_data_from_csv_average_function(
        link="https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"
    )
    return render_template("average.html", average=average)


@app.route("/get-content/")
def get_content():
    to_create_file(file_name="text")  # put application's code here
    get_content_from_file = to_read_file(file_name="text")
    return render_template("get_content_from_file.html", get_content_from_file=get_content_from_file)


if __name__ == "__main__":
    app.run()
