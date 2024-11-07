import psycopg2
from psycopg2 import sql
import sqlite3
postgres_conn_params = {
    'dbname': 'postgres',  # Default database
    'user': 'postgres',
    'password': 'qwerty',  # Replace with your postgres user's password
    'host': 'localhost',
    'port': 5432
}
def create_postgres_user_and_db(cursor, new_user, new_password, new_db):
    try:
        # Create a new user
        cursor.execute(sql.SQL("CREATE USER {} WITH PASSWORD %s;").format(sql.Identifier(new_user)), [new_password])
        print(f"User '{new_user}' created.")
    except psycopg2.errors.DuplicateObject:
        print(f"User '{new_user}' already exists.")

    try:
        # Create a new database owned by the new user
        cursor.execute(sql.SQL("CREATE DATABASE {} OWNER {};").format(sql.Identifier(new_db), sql.Identifier(new_user)))
        print(f"Database '{new_db}' created with owner '{new_user}'.")
    except psycopg2.errors.DuplicateDatabase:
        print(f"Database '{new_db}' already exists.")


if __name__ == '__main__':
    try:
        # Attempt to connect to PostgreSQL
        postgres_conn = psycopg2.connect(**postgres_conn_params)
        postgres_conn.autocommit = True  # Enable autocommit for DDL statements
        postgres_cursor = postgres_conn.cursor()
        print("Connected to PostgreSQL.")
    except psycopg2.OperationalError as e:
        print("PostgreSQL is not available. Falling back to SQLite.")
        postgres_conn = None