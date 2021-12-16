#!/usr/bin/python3
"""
    0-select_states.py
    module
    return: nothing
"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    if len(argv) < 5:
        raise ValueError("must have 5 args")
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT name FROM states")
    query_rows = cur.fetchall()
    names = []
    for row in query_rows:
        names.append(row[0])
    if argv[4] in names:
        cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4]))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    cur.close()
    conn.close()
