#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page - Show all trips
#-----------------------------------------------------------
@app.get("/")
def show_trips():
    with connect_db() as db:
        sql = """
            SELECT id, Trip_Name, Trip_Budget, Trip_Activitys_Code
            FROM trips
            ORDER BY id
        """

        trips = db.execute(sql).fetchall()

        return render_template(
            "pages/_Trips.jinja",
            trips=trips
        )


#-----------------------------------------------------------
# Trips page
#-----------------------------------------------------------
@app.get("/Trips")
def trips_page():
    with connect_db() as db:
        sql = """
            SELECT id, Trip_Name, Trip_Budget, Trip_Activitys_Code
            FROM trips
            ORDER BY id
        """

        trips = db.execute(sql).fetchall()

        return render_template(
            "pages/_Trips.jinja",
            trips=trips
        )



#-----------------------------------------------------------
# Trips page
#-----------------------------------------------------------
@app.get("/trip/<int:trip_id>")
def view_trip(trip_id):

    with connect_db() as db:

        trip = db.execute("""
            SELECT *
            FROM trips
            WHERE id = ?
        """, (trip_id,)).fetchone()

        if trip is None:
            return "Trip not found", 404

        activities = db.execute("""
            SELECT *
            FROM Activitys
            WHERE Code = ?
        """, (trip["Trip_Activitys_Code"],)).fetchall()

        return render_template(
            "pages/_Trip.jinja",
            trip=trip,
            activities=activities
        )



#-----------------------------------------------------------
# Add Activity
#-----------------------------------------------------------
@app.route("/add_activity", methods=["GET", "POST"])
def add_activity():

    if request.method == "POST":

        activity_name = request.form["Activity_Name"]
        activity_location = request.form["Activity_Location"]
        activity_hours = request.form["Activity_Houers"]
        activity_price = request.form["Activity_Price"]
        activity_info = request.form["Activity_info"]
        activity_img = request.form["Activity_IMG"]

        with connect_db() as db:

            db.execute("""
                INSERT INTO Activitys
                (
                    Activity_Name,
                    Activity_Location,
                    Activity_Houers,
                    Activity_Price
                    Activity_info,
                    Activity_IMG
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                activity_name,
                activity_location,
                activity_hours,
                activity_price,
                activity_info,
                activity_img
            ))

        return redirect("/")

    return render_template("pages/_Activity_Form.jinja")

#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

