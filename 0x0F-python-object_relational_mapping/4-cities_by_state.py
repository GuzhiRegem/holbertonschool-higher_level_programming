#!/usr/bin/python3
"""
    0-select_states.py
    module
    return: nothing
"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    if len(argv) < 4:
        raise ValueError("must have 4 args")
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
