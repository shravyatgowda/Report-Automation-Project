import sqlite3

def run_query(database, query):
    """Runs a SQL query on a SQLite database and prints the results."""
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        print("Query executed successfully.")
        for row in results:
            print(row)
    except Exception as e:
        print(f"Error running query: {e}")

def generate_select_query(table, columns="*", conditions=None):
    """Generates a SELECT SQL query."""
    query = f"SELECT {columns} FROM {table}"
    if conditions:
        query += f" WHERE {conditions}"
    return query

def generate_insert_query(table, data):
    """Generates an INSERT SQL query."""
    columns = ', '.join(data.keys())
    values = ', '.join([f"'{v}'" for v in data.values()])
    query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
    return query

def generate_update_query(table, updates, condition):
    """Generates an UPDATE SQL query."""
    set_clause = ', '.join([f"{k}='{v}'" for k, v in updates.items()])
    query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
    return query

def generate_delete_query(table, condition):
    """Generates a DELETE SQL query."""
    return f"DELETE FROM {table} WHERE {condition}"


