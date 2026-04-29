from flask import Flask, render_template, request

app = Flask(__name__)

def get_route_options(start_location, destination):
    """Creates placeholder route options for the SafePath app."""

    routes = {
        "safest_route": {
            "name": "Safest Route",
            "description": "A route that avoids higher-risk areas and prioritizes safer travel.",
            "estimated_time": "28 minutes"
        },
        "fastest_route": {
            "name": "Fastest Route",
            "description": "A route that focuses on the shortest estimated travel time.",
            "estimated_time": "21 minutes"
        },
        "recommended_route": {
            "name": "Recommended Route",
            "description": "A balanced option that considers both safety and speed.",
            "estimated_time": "24 minutes"
        }
    }

    return routes


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/route", methods=["POST"])
def route():
    start_location = request.form.get("start_location")
    destination = request.form.get("destination")

    route_options = get_route_options(start_location, destination)

    return render_template(
        "route.html",
        start_location=start_location,
        destination=destination,
        routes=route_options
    )


if __name__ == "__main__":
    app.run(debug=True)
