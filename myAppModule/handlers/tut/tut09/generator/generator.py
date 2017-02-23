import os
import random
import string
import sqlite3

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))
DB_STRING = "my.db"

class StringGeneratorWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        with sqlite3.connect(DB_STRING) as c:
            c.execute("SELECT value FROM TUT09string WHERE session_id=?",
                      [cherrypy.session.id])
            return c.fetchone()

    def POST(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        with sqlite3.connect(DB_STRING) as c:
            c.execute("INSERT INTO TUT09string VALUES (?, ?)",
                      [cherrypy.session.id, some_string])
        return some_string

    def PUT(self, another_string):
        with sqlite3.connect(DB_STRING) as c:
            c.execute("UPDATE TUT09string SET value=? WHERE session_id=?",
                      [another_string, cherrypy.session.id])

    def DELETE(self):
        with sqlite3.connect(DB_STRING) as c:
            c.execute("DELETE FROM TUT09string WHERE session_id=?",
                      [cherrypy.session.id])

def setup_database():
    """
    Create the `TUT09string` table in the database
    on server startup
    """
    with sqlite3.connect(DB_STRING) as con:
        con.execute("CREATE TABLE TUT09string (session_id, value)")

def cleanup_database():
    """
    Destroy the `TUT09string` table from the database
    on server shutdown.
    """
    with sqlite3.connect(DB_STRING) as con:
        con.execute("DROP TABLE TUT09string")

cherrypy.engine.subscribe('start', setup_database)
cherrypy.engine.subscribe('stop', cleanup_database)
