import psycopg2
from psycopg2 import sql
import sqlite3

from consts import db_logger
from db_classes import PostgreSQL, SQLite

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
    if SQLite.search_for_sql():
        db = PostgreSQL()
    else: 
        db = SQLite()
    print(f"We are using {db.__class__.__name__}")

    db.create_user('Seva', 'qwerty')


    print(1)