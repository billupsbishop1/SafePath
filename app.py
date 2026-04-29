from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/route", methods=["POST"])
def route():
    start_location = request.form["start_location"]
    destination = request.form["destination"]

    safest_route = "Take the main roads with better lighting and more public activity."
    fastest_route = "Take the shortest available route based on estimated travel time."
    recommended_route = "Use the safest route if traveling at night or in an unfamiliar area."

    return render_template(
        "route.html",
        start_location=start_location,
        destination=destination,
        safest_route=safest_route,
        fastest_route=fastest_route,
        recommended_route=recommended_route
    )

if __name__ == "__main__":
    app.run(debug=True)
