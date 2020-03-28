#!/usr/bin/python3
# Comment
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = connection.cursor()
    execute = cursor.execute("SELECT id, name FROM states ORDER BY states.id;")
    for i in range(0, execute):
        print(cursor.fetchone())
    cursor.close()
    connection.close()
