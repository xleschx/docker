from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return f"""<html>
                <head>
                    <title>Demo for Docker</title>
                </head>
                <body>
                  <h1>Welcome to this demo for Docker</h1>
                    <h2>This is a project for school purposes</h2>
                    <p>Test1</p>
                </body>
            </html>"""

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
