#!/usr/bin/python3
# Comment
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = connection.cursor()
    execute = cursor.execute("SELECT cities.id, cities.name, states.name \
                              FROM cities JOIN states\
                              ON cities.state_id = states.id\
                              ORDER BY cities.id;")
    for i in range(0, execute):
        entry = cursor.fetchone()
        print(entry)
    cursor.close()
    connection.close()
