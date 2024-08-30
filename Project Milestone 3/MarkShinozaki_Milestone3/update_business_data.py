# Mark Shinozaki
# Cpts 451
# This file was used to generate Queries 

import psycopg2

def calculate_and_update_business_data():
    try:
        conn = psycopg2.connect("dbname='milestone1DB' user='postgres' host='localhost' password='jn&!!8tCK6H'")
        cur = conn.cursor()
    except Exception as e:
        print('Unable to connect to the database!', e)
        return

    # Calculate numCheckins
    print("Updating numCheckins...")
    cur.execute("""
        UPDATE business b
        SET numcheckins = subquery.total_checkins
        FROM (
            SELECT business_id, SUM(count) as total_checkins
            FROM checkintable
            GROUP BY business_id
        ) AS subquery
        WHERE b.business_id = subquery.business_id;
    """)
    conn.commit()

    # Verify numCheckins update
    cur.execute("SELECT business_id, numcheckins FROM business LIMIT 10;")
    for row in cur.fetchall():
        print(f"Business ID: {row[0]}, NumCheckins: {row[1]}")

    # Calculate reviewcount
    print("Updating reviewcount...")
    cur.execute("""
        UPDATE business b
        SET reviewcount = subquery.total_reviews
        FROM (
            SELECT business_id, COUNT(*) as total_reviews
            FROM reviewtable
            GROUP BY business_id
        ) AS subquery
        WHERE b.business_id = subquery.business_id;
    """)
    conn.commit()

    # Verify reviewcount update
    cur.execute("SELECT business_id, reviewcount FROM business LIMIT 10;")
    for row in cur.fetchall():
        print(f"Business ID: {row[0]}, ReviewCount: {row[1]}")

    # Calculate reviewrating
    print("Updating reviewrating...")
    cur.execute("""
        UPDATE business b
        SET reviewrating = ROUND(subquery.avg_rating, 2)
        FROM (
            SELECT business_id, AVG(stars) as avg_rating
            FROM reviewtable
            GROUP BY business_id
        ) AS subquery
        WHERE b.business_id = subquery.business_id;
    """)
    conn.commit()

    # Verify reviewrating update
    cur.execute("SELECT business_id, reviewrating FROM business LIMIT 10;")
    for row in cur.fetchall():
        print(f"Business ID: {row[0]}, ReviewRating: {row[1]}")

    cur.close()
    conn.close()

    print("Business table updated successfully.")

# Execute the function
calculate_and_update_business_data()
