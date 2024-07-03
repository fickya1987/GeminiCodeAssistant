import sqlite3

# Connect to SQLite
conn = sqlite3.connect("student.db")

# Create cursor object
cursor = conn.cursor()

# Create table
table_info = """
create table if not exists student(
id integer primary key autoincrement,
name varchar(30),
class varchar(20),
section varchar(25),
marks int);
"""

try:
    cursor.execute(table_info)
    print("Table created successfully or already exists.")

    # Insert records
    records = [
        ('Tanzila', 'Data Science', 'B', 85),
        ('Ali', 'Data Science', 'B', 95),
        ('Nazhat', 'Data Science', 'A', 80),
        ('Afreen', 'Data Science', 'B', 86),
        ('Ishrat', 'Data Science', 'B', 55),
        ('Sara', 'Data Science', 'A', 78),
        ('Ahmed', 'Data Science', 'C', 92),
        ('Fatima', 'Data Science', 'A', 88),
        ('John', 'Data Science', 'C', 75),
        ('Lina', 'Data Science', 'B', 68),
        ('Omar', 'Data Science', 'A', 83),
        ('Kiran', 'Data Science', 'C', 91)
    ]

    cursor.executemany("insert into student (name, class, section, marks) values (?, ?, ?, ?)", records)
    print("Records inserted successfully.")

    # Commit the changes
    conn.commit()

    # Display the inserted records
    print("The inserted records are:")

    data = cursor.execute("select * from student")

    for row in data:
        print(row)

except sqlite3.Error as error:
    print(f"Error while executing sqlite script: {error}")
finally:
    # Close the connection
    conn.close()
    print("SQLite connection closed.")
