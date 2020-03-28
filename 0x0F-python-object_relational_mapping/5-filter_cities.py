#!/usr/bin/python3
# Comment
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    connection = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = connection.cursor()
    execute = cursor.execute("SELECT cities.name FROM cities JOIN states\
                             ON cities.state_id = states.id\
                             WHERE states.name=%(s_name)s ORDER BY cities.id\
                             ", {'s_name': argv[4]})
    entries = cursor.fetchall()
    print(", ".join(entry[0] for entry in entries))
    cursor.close()
    connection.close()
