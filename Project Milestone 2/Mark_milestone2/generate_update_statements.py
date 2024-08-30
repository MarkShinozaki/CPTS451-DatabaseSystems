import psycopg2

def generate_update_statements():
    try:
        conn = psycopg2.connect("dbname='milestone1DB' user='postgres' host='localhost' password='jn&!!8tCK6H'")
        cur = conn.cursor()
    except Exception as e:
        print('Unable to connect to the database!', e)
        return

    update_statements = []

    # Generate numCheckins update statements
    cur.execute("""
        SELECT business_id, SUM(count) as total_checkins
        FROM checkintable
        GROUP BY business_id;
    """)
    for row in cur.fetchall():
        business_id, total_checkins = row
        update_statements.append(f"UPDATE business SET numcheckins = {total_checkins} WHERE business_id = '{business_id}';")

    # Generate reviewcount update statements
    cur.execute("""
        SELECT business_id, COUNT(*) as total_reviews
        FROM reviewtable
        GROUP BY business_id;
    """)
    for row in cur.fetchall():
        business_id, total_reviews = row
        update_statements.append(f"UPDATE business SET reviewcount = {total_reviews} WHERE business_id = '{business_id}';")

    # Generate reviewrating update statements
    cur.execute("""
        SELECT business_id, ROUND(AVG(stars), 2) as avg_rating
        FROM reviewtable
        GROUP BY business_id;
    """)
    for row in cur.fetchall():
        business_id, avg_rating = row
        update_statements.append(f"UPDATE business SET reviewrating = {avg_rating} WHERE business_id = '{business_id}';")

    cur.close()
    conn.close()

    # Write update statements to file
    with open('MarkShinozaki_UPDATE.sql', 'w') as f:
        for statement in update_statements:
            f.write(statement + '\n')

    print("Update statements generated successfully and written to MarkShinozaki_UPDATE.sql")

# Execute the function
generate_update_statements()
