import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO kids (username, city, latitude, longitude) VALUES (?, ?, ?, ?)", ('john', 'Kelowna', 0, 0))
cur.execute("INSERT INTO kids (username, city, latitude, longitude) VALUES (?, ?, ?, ?)", ('arnold', 'Vancouver', 0, 0))

cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Vancouver", 49.28349702140323, -123.10725284748895))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Kelowna", 49.88420995754495, -119.49357503076985))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Victoria", 48.4287476406036, -123.36628105217467))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Calgary", 51.080313671377276, -114.01862123015518))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Edmonton", 53.54953220073074, -113.51814314417118))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Red Deer",52.26894117548524, -113.80997727758995))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Saskatoon", 52.15763584193717, -106.67368021863426))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Regina", 50.44547814138211, -104.62133286971792))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Prince Albert", 53.20407878747699, -105.74624699213712))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Winnipeg", 49.897588833257245, -97.15318318007348))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Brandon", 49.84425144539961, -99.95096082564714))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Steinbach", 49.53031727059315, -96.69036614179785))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Toronto", 43.65518162658108, -79.37428151006742))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Ottawa", 45.42006100317143, -75.67254086812672))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Missisauga", 43.59025841791699, -79.6103908525925))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ("Montreal", 45.50001686524721, -73.56046802510579))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ('Quebec City', 46.81754599838052, -71.22949693212746))
cur.execute("INSERT INTO city (cname, latitude, longitude) VALUES (?, ?, ?)", ('Gatineau', 45.476833180693255, -75.7100104653505))


connection.commit()
connection.close()