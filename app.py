from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main():
    message = "Hello world!"
    return render_template('index.html', message = message)

if __name__ == "__main__":
    app.run()