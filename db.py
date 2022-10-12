import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            contact text,
            vehicle text,
            number text,
            vehicleName text,
            email text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, contact, vehicle, number, vehicleName, email, address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                         (name, contact, vehicle, number, vehicleName, email, address))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from employees where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, contact, vehicle, number, vehicleName, email, address):
        self.cur.execute(
            "update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
            (name, contact, vehicle, number, vehicleName, email, address, id))
        self.con.commit()