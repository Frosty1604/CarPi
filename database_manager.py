import sqlite3
import csv


def create_connection():
    try:
        conn = sqlite3.connect("car_pi_database.db")
        return conn
    except Exception as e:
        print(e)

    return None


def create_table():
    sql_create_table_logger = """CREATE TABLE IF NOT EXISTS car_stats (
                                        id text PRIMARY KEY,
                                        speed text NOT NULL,
                                        rpm text NOT NULL,
                                        engine_runtime text NOT NULL,
                                        throttle_pos text NOT NULL,
                                        fuel_level text NOT NULL, 
                                        fuel_rate text NOT NULL, 
                                        coolant_temp text NOT NULL,
                                        oil_temp text NOT NULL, 
                                        engine_load text NOT NULL
                                    ); """
    conn = create_connection()
    try:
        conn.execute(sql_create_table_logger)
    except Exception as e:
        print(e)
    finally:
        conn.close()


def add_data(data):
    sql_add_data = """INSERT INTO car_stats (
    id, speed, rpm, engine_runtime, throttle_pos, fuel_level, fuel_rate, coolant_temp, oil_temp, engine_load) 
    VALUES (?,?,?,?,?,?,?,?,?,?)"""
    conn = create_connection()
    try:
        conn.execute(sql_add_data, data)
        conn.commit()
    except Exception as exception:
        print(exception)
    finally:
        conn.close()


def export_data_from_db():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM car_stats")

    with open("car_pi_stats.csv", "w") as out_csv_file:
        csv_out = csv.writer(out_csv_file)
        csv_out.writerow([data[0] for data in cursor.description])  # header

        for result in cursor:  # data
            csv_out.writerow(result)

    conn.close()
