import psycopg2
import datetime
import pandas as pd
conn = None
try:
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host="devtradingsagedb-do-user-12481132-0.b.db.ondigitalocean.com",
        database="defaultdb",
        user="doadmin",
        password="AVNS_AZ-3Q1oUpp9WnsReBBX",
        port=25060,
        sslmode='require',
    )
    date1 = list(map(int, input("Write first date(day/month/year) ").split('/')))
    date2 = list(map(int, input("Write second date(day/month/year) ").split('/')))
    cur = conn.cursor()
    cur.execute(f"SELECT*FROM test_assignment where date='{date1[2]}-{date1[1]}-{date1[0]}'")
    data1 = cur.fetchall()
    cur.execute(f"SELECT*FROM test_assignment where date='{date2[2]}-{date2[1]}-{date2[0]}'")
    data2 = cur.fetchall()
    answers = {}
    for i in data2: answers[f'{i[2]} {i[3]}']=i[5]
    for i in data1: answers[f'{i[2]} {i[3]}']-=i[5]
    x, y, z = [], [], []
    for i in answers:
        strike, instrument_type = i.split()
        x.append(instrument_type)
        y.append(int(strike))
        z.append(answers[i])
    df1 = pd.DataFrame({"Instrument type":x, "Strike":y, "Difference":z})
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print(df1)
    cur.close()
except (Exception, psycopg2.DatabaseError) as error: print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')


['date', 'ticker', 'strike', 'instrument_type', 'expiry_date', 'oi', 'underlying', 'last_update']