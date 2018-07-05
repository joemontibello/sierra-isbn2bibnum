#!/usr/local/bin/python3

import psycopg2

# Open a file, get a line, assume it's an ISBN, send it as an sql query, get back bib record numbers ready for import
# into a review file.
inputfile = './inputfile.txt'
credfile = '../credfile.txt'
outputfile = './outputfile.txt'

# creds opens the file that holds usernames and passwords. I don't include that file in this directory so I can't
# accidentally upload my username and password to github!
try:
    creds = open(credfile, 'r')
except IOError:
    print("Failed to open credential store at " + credfile + "\n")
    raise
else:
        username = creds.readline().rstrip()
        password = creds.readline().rstrip()
        creds.close()
if username == "" or password == "":
    print("Failed to read one or more of the needed credentials from " + credfile + "\n")

params = {
  'dbname': 'iii',
  'user': username,
  'password': password,
  'host': 'sierra-db.dartmouth.edu',
  'port': '1032',
  'sslmode': 'require'
}

try:
    isbns = open(inputfile, 'r')
except IOError:
    print("Failed to open file of isbns at " + inputfile + "\n")
    raise
else:
    outfile = open(outputfile, "w")
    for thisisbn in iter(isbns.readline, ''):
        # print(thisisbn)
        thisisbn = thisisbn.rstrip()
        sqlquery = "SELECT id2reckey(record_id) || 'a' FROM sierra_view.phrase_entry WHERE index_tag || index_entry LIKE 'i' || '" + thisisbn + "' || '%'"
        # print(sqlquery)
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sqlquery)
        for record in cur:
            # print(record)
            outfile.write(str(record)+'\n')
        cur.close()
        conn.close()
    outfile.close()