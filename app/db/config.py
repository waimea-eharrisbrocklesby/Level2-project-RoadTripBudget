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
            Trip_Activitys_Code  INTEGER
        )
    """

    SEED_DATA = """
        INSERT INTO trips (Trip_Name, Trip_Budget, Trip_Activitys_Code)
        VALUES
    
    -------|  Trip_Name  |  Trip_Budget  |  Trip_Activitys_Code  |-------
        (     "Demo_Trip",       800,                  1            ),
        (     "Demo_Trip2",      1000,                 2            ),
        (     "Demo_Trip3",      500,                  3            )
    """

# Add more table classes here...
class Activitys_Table:

    NAME = "Activitys"

    SCHEMA = """
        CREATE TABLE Activitys (
            Code                     INTEGER PRIMARY KEY AUTOINCREMENT,
            Activity_Name            INTEGER DEFAULT 0,
            Activity_Location        TEXT NOT NULL,
            Activity_Houers          INTEGER,
            Activity_Price           INTEGER DEFAULT 0,
            Activity_info            TEXT,
            Activity_IMG             TEXT
        )
    """

    SEED_DATA = """
        INSERT INTO Activitys (Code, Activity_Name, Activity_Location, Activity_Houers, Activity_Price, Activity_info, Activity_IMG)
        VALUES
    
    -------|  Code  |  Activity_Name  |  Activity_Location  |  Activity_Houers  |  Activity_Price  |  Activity_info  |  Activity_IMG  |-------
        (      1,      "Demo_Activity",    "Demo_Location",           2,                  100,          "Demo_Info",     "Demo_IMG"      ),
        (      2,      "Demo_Activity2",   "Demo_Location2",          3,                  150,          "Demo_Info2",    "Demo_IMG2"     ),
        (      3,      "Demo_Activity3",   "Demo_Location3",          4,                  200,          "Demo_Info3",    "Demo_IMG3"     )
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

