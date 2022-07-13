import psycopg2

class sqlConnector:
    
    conn=None
    
    
    #  This constructor specifies various parameters required for proper connection to the Postgres database
    def __init__(self):
        self.conn=psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Ayush@37")
        
    # used to insert an entry into database.
    def insertIntoTable(self, fileName, encoding):
        cur = self.conn.cursor()
        cur.execute("insert into imgtable(filename, vector) values('" + fileName+"', ARRAY "+encoding+");")
        self.conn.commit()
        self.conn.close()
    
    # This function is used to select all rows from the table
    def selectAll(self):
        cur = self.conn.cursor()
        cur.execute("select * from imgtable;")
        records=cur.fetchall()
        self.conn.close()
        return records
    
    # used to fetch a row corresponding to id provided as a parameter
    def selectAgainstId(self, id):
        query="select * from imgtable where id="+id+";"
        cur = self.conn.cursor()
        cur.execute(query)
        records=cur.fetchall()
        self.conn.close()
        return records
    
    # update meta data field in the table corresponding to the id provided as parameter
    def update_meta_data(self, id, person_name, version, location, date):
        cur = self.conn.cursor()
        query="update imgtable set personname='" + person_name+"', version="+version+", location='" + location+"', date='" + date+"' where id="+id+";"
        cur.execute(query)
        self.conn.commit()
        self.conn.close()
    
    
    
    
    
