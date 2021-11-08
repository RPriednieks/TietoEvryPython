import sqlite3


def create_connection(dbpath='chinook.db'):
    con = sqlite3.connect(dbpath)
    cursor = con.cursor()
    return cursor


cur = create_connection()


def read_artists(cur):  # can add some extra parameters to limit
    cur.execute('SELECT * FROM artists')
    return cur.fetchall()  # can return a list of tuples, or you can create a list of artist objects if you want

artists = read_artists(cur)
print(artists)


# def create_artist(conn, artist_name):
#
#   # do not have to return anything but can use try: inside this function
#
# def update_artist(id, new_name):
#
# def delete_artist(id=None, name=""):
#
#    # provide deletion by id AND/OR name
#
#
#
# test it by adding you name to artists table smile
