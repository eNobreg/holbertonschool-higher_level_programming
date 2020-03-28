#!/usr/bin/python3
# Comment
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = connection.cursor()
    execute = cursor.execute("SELECT id, name FROM states\
                          WHERE states.name=%(state)s\
                          ORDER BY states.id;", {'state': argv[4]})
    for i in range(0, execute):
        entry = cursor.fetchone()
        print(entry)
    cursor.close()
    connection.close()
