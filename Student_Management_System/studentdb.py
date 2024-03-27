import mysql.connector

class StudentDatabase:
    def __init__(self):
        try:
            self.my_conn=mysql.connector.connect(
                            host='localhost', 
                            user='root', 
                            password='23112017@28082018', 
                            database='student_management')
            self.cur=self.my_conn.cursor() 
            self.db_query="CREATE TABLE if not exists student(ID INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(30),last_name VARCHAR(30), gender VARCHAR(7),dob VARCHAR(15),department VARCHAR(20),contact VARCHAR(15), email VARCHAR(40), address VARCHAR(200))"
            self.cur.execute(self.db_query)
            self.my_conn.commit()
        #To let auto increment starts with 101
            self.db_query="ALTER TABLE student AUTO_INCREMENT=101"
            self.cur.execute(self.db_query)
            self.my_conn.commit()
            self.my_conn.close
        except mysql.connector.Error as err:
            print("Error:", f"Due to{str(err)}")
            # Handle the error here, such as logging or displaying a message to the user    
    
    #Insert Function
    def stu_insert(self, new_data):
        """
    Insert a new student record into the database.

    This method inserts a new student record into the 'student' table of the database. It first establishes a connection
    to the database, creates a cursor object, and then executes an SQL query to insert the new data into the table.
    After the insertion, it commits the changes to the database and closes the connection.

    Args:
        new_data (tuple): A tuple containing the data for the new student record.

    Returns:
        None
    """
        try:
            self.my_conn=mysql.connector.connect(
                            host='localhost', 
                            user='root', 
                            password='23112017@28082018', 
                            database='student_management')
            self.cur=self.my_conn.cursor() 
            self.db_query="INSERT INTO student VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.cur.execute(self.db_query,new_data)
            self.my_conn.commit()
            self.my_conn.close
        except mysql.connector.Error as err:
             print("Error:", f"Due to{str(err)}")
            # Handle the error here, such as logging or displaying a message to the user
        
     #Fetch all data from Database   
    def fetch_data(self):
            """
    Retrieve all student records from the database.

    This method fetches all student records from the 'student' table in the database. It establishes a connection to
    the database, creates a cursor object, executes an SQL query to select all records, fetches the results, commits
    any changes made, and then closes the connection.

    Returns:
        list: A list containing tuples representing each student record fetched from the database.
    """
            self.my_conn=mysql.connector.connect(
                            host='localhost', 
                            user='root', 
                            password='23112017@28082018', 
                            database='student_management')
            self.cur=self.my_conn.cursor() 
            self.cur.execute("SELECT * FROM student;")
            rows=self.cur.fetchall()
            self.my_conn.commit()
            self.my_conn.close
            return rows
            
    
    #Delete a record in Database

    def stu_delete(self,id):
        """
    Delete a student record from the database based on the provided ID.

    This method attempts to delete a student record from the 'student' table in the database based on the provided ID.
    It establishes a connection to the database, creates a cursor object, executes an SQL DELETE query using the
    provided ID, commits any changes made, and then closes the connection.

    Args:
        id (int): The ID of the student record to be deleted.

    Returns:
        None
    """
        try:
            self.my_conn=mysql.connector.connect(
                            host='localhost', 
                            user='root', 
                            password='23112017@28082018', 
                            database='student_management')
            self.cur=self.my_conn.cursor() 
            self.cur.execute("DELETE FROM student WHERE ID=%s",(id,))
            self.my_conn.commit()
            self.my_conn.close()
        except mysql.connector.Error as err:
             print("Error:", f"Due to{str(err)}")
            # Handle the error here, such as logging or displaying a message to the user

    #Update fields in Database
        
    def stu_update(self,id,fname,lname,gender,dob,dept,cont,email,addr):
        """
    Update a student record in the database.

    This method attempts to update a student record in the 'student' table of the database based on the provided ID.
    It establishes a connection to the database, creates a cursor object, executes an SQL UPDATE query with the provided
    data, commits any changes made, and then closes the connection.
    """
        try:
            self.my_conn=mysql.connector.connect(
                            host='localhost', 
                            user='root', 
                            password='23112017@28082018', 
                            database='student_management')
            self.cur=self.my_conn.cursor() 
            self.cur.execute("UPDATE student SET first_name=%s,last_name=%s,gender=%s,dob=%s,department=%s, contact=%s,email=%s,address=%s WHERE ID=%s",
                         (fname,lname,gender,dob,dept,cont,email,addr,id))
            self.my_conn.commit()
            self.my_conn.close()
        except mysql.connector.Error as err:
             print("Error:", f"Due to{str(err)}")
            # Handle the error here, such as logging or displaying a message to the user


#Search fields in Database
    def stu_search(self,com_search,ent_search):
        """
    Search for student records in the database.

    This method searches for student records in the 'student' table of the database based on the specified search criteria.
    It establishes a connection to the database, creates a cursor object, executes an SQL SELECT query with the provided
    search parameters, fetches the matching rows, commits any changes made, and then closes the connection.

    Args:
        com_search (str): The column name to search within (e.g., 'first_name', 'last_name', 'email').
        ent_search (str): The search term to match against.

    Returns:
        list: A list of tuples containing the matching student records.
    """
        self.my_conn=mysql.connector.connect(
                            host='localhost', 
                            user='root', 
                            password='23112017@28082018', 
                            database='student_management')
        self.cur=self.my_conn.cursor() 
        query = "SELECT * FROM student WHERE {} LIKE %s".format(com_search)
        self.cur.execute(query, ('%' + ent_search + '%',))
        rows=self.cur.fetchall()
        self.my_conn.commit()
        self.my_conn.close
        return rows


stu_obj=StudentDatabase()
