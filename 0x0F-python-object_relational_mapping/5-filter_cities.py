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
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = '{}' ORDER BY cities.id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    names = []
    for row in query_rows:
        names.append(row[0])
    print(*names, sep=", ")
    cur.close()
    conn.close()
