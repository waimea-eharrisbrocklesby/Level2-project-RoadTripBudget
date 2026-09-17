#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class Trip_Table:

    NAME = "trips"

    SCHEMA = """
        CREATE TABLE trips (
            id                   INTEGER PRIMARY KEY AUTOINCREMENT,
            Trip_Name            TEXT NOT NULL,
            Trip_Budget          INTEGER DEFAULT 0,
            Trip_Activitys_Code  TEXT DEFAULT (lower(hex(randomblob(4))))
        );
        
    """

    SEED_DATA = """
        INSERT INTO trips (Trip_Name, Trip_Budget, Trip_Activitys_Code)
        VALUES
    
    -------|  Trip_Name     |  Trip_Budget  |  Trip_Activitys_Code |-------
        (     "Demo_Trip",       800,                "abc"         ),
        (     "Demo_Trip2",      1000,               "def"         ),
        (     "Demo_Trip3",      500,                "ghi"         )
    """

# Add more table classes here...Name
class Activitys_Table:

    NAME = "Activitys"

    SCHEMA = """
        CREATE TABLE Activitys (
            id                       INTEGER PRIMARY KEY AUTOINCREMENT,
            Code                     TEXT NOT NULL,
            Activity_Name            TEXT NOT NULL,
            Activity_Location        TEXT NOT NULL,
            Activity_Houers          INTEGER,
            Activity_Price           INTEGER DEFAULT 0,
            Activity_info            TEXT,
            Activity_IMG             TEXT
        )
    """

    SEED_DATA = """
        INSERT INTO Activitys 
        (Code, Activity_Name, Activity_Location, Activity_Houers, Activity_Price, Activity_info, Activity_IMG)
        VALUES

        -------|  Code  |  Activity_Name       |  Activity_Location  |  Activity_Houers  |  Activity_Price  |  Activity_info                           |  Activity_IMG          |-------

        (          "abc",       "Kayaking",             "Abel Tasman",            3,                120,          "Explore the coastline by kayak.",        "kayaking.jpg"             ),
        (          "abc",       "Beach Walk",            "Torrent Bay",           2,                20,           "Walk along the beautiful beach.",         "beach_walk.jpg"          ),
        (          "abc",       "Water Taxi",            "Marahau",               1,                80,           "Take a water taxi along the coast.",      "water_taxi.jpg"          ),
        (          "abc",       "Forest Hike",           "Abel Tasman",           4,                35,           "Hike through native New Zealand forest.", "forest_hike.jpg"         ),

        (          "def",       "Mountain Biking",       "Nelson",                3,                90,           "Ride through scenic mountain trails.",    "mountain_biking.jpg"     ),
        (          "def",       "Ziplining",             "Nelson",                2,               110,           "Fly through the forest canopy.",           "ziplining.jpg"          ),
        (          "def",       "Rock Climbing",         "Nelson",                3,                75,           "Try climbing some local rock faces.",     "rock_climbing.jpg"       ),
        (          "def",       "Quad Biking",           "Nelson",                2,               140,           "Explore the countryside on a quad bike.", "quad_biking.jpg"         ),

        (          "ghi",       "City Tour",             "Nelson",                2,                30,           "Explore the main sights around Nelson.",  "city_tour.jpg"           ),
        (          "ghi",       "Museum Visit",          "Nelson",                2,                15,           "Learn about local history and culture.",  "museum.jpg"              ),
        (          "ghi",       "Botanical Walk",        "Nelson",                1,                10,           "Take a relaxing walk through gardens.",   "botanical_walk.jpg"      ),
        (          "ghi",       "Cafe Tour",             "Nelson",                3,                45,           "Visit some of Nelson's best cafes.",      "cafe_tour.jpg"           )
    """



#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Note: The table o
# rder is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    Trip_Table,
    Activitys_Table,
    # Add more tables here...
]

