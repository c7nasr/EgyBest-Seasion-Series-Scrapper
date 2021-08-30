class MyServer:
    def __init__(self):
        self.globalData = "hello"


from core import EgybestLogic
from flask import Flask

app = Flask(__name__)

my_server = EgybestLogic()


@app.route("/")
def getSomeData():
    my_server.state = "season"
    my_server.url = "https://lack.egybest.fyi/season/chapelwaite-season-1/?"
    my_server.base_domain = my_server.url.split("/")[2]
    my_server.fetch_info()
    my_server.single_episode_info()
    return my_server.url


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
