
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template("main_page.html")


@app.route('/dashboard/')
def dashboard():
    return
    #return render_template("main_page.html")



if __name__ == "__main__":
    app.run()

