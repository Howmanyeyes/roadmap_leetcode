"""Classes for DB interactions"""

import psycopg2
import sqlite3
import logging

# Assuming db_logger is defined in consts.py
from consts import db_logger

class AbstractDB:
    """Abstract class for DB; used to determine if PostgreSQL exists."""

    @staticmethod
    def search_for_sql():
        postgres_conn_params = {
            'dbname': 'postgres',  # Default database
            'user': 'postgres',
            'password': 'qwerty',  # Replace with your postgres user's password
            'host': 'localhost',
            'port': 5432
        }
        try:
            postgres_conn = psycopg2.connect(**postgres_conn_params)
            postgres_conn.close()
            db_logger.info("Connected to PostgreSQL.")
            return True
        except psycopg2.OperationalError:
            db_logger.info("PostgreSQL is not available. Falling back to SQLite.")
            return False

class PostgreSQL(AbstractDB):
    def __init__(self, admin_user='postgres', admin_password='qwerty', host='localhost', port=5432):
        self.admin_conn_params = {
            'dbname': 'postgres',
            'user': admin_user,
            'password': admin_password,
            'host': host,
            'port': port
        }
        self.user_conn_params = None
        self.conn = None
        self.user = None
        self.password = None

    def create_user(self, new_user, new_password):
        """Create a new PostgreSQL user with a password and log in as that user."""
        try:
            # Connect as admin user
            with psycopg2.connect(**self.admin_conn_params) as admin_conn:
                admin_conn.autocommit = True
                with admin_conn.cursor() as cursor:
                    # Create new user with password
                    cursor.execute(
                        psycopg2.sql.SQL("CREATE USER {} WITH PASSWORD %s;").format(
                            psycopg2.sql.Identifier(new_user)
                        ),
                        [new_password]
                    )
                    db_logger.info(f"User '{new_user}' created in PostgreSQL.")

            # Update connection parameters to use the new user
            self.user_conn_params = {
                'dbname': 'postgres',  # Connect to the default database
                'user': new_user,
                'password': new_password,
                'host': self.admin_conn_params['host'],
                'port': self.admin_conn_params['port']
            }
            self.user = new_user
            self.password = new_password

            # Connect as the new user
            self.conn = psycopg2.connect(**self.user_conn_params)
            db_logger.info(f"Logged in as user '{new_user}' in PostgreSQL.")

        except psycopg2.errors.DuplicateObject:
            db_logger.warning(f"User '{new_user}' already exists in PostgreSQL.")
            # Attempt to connect as the existing user
            self.user_conn_params = {
                'dbname': 'postgres',
                'user': new_user,
                'password': new_password,
                'host': self.admin_conn_params['host'],
                'port': self.admin_conn_params['port']
            }
            self.user = new_user
            self.password = new_password
            try:
                self.conn = psycopg2.connect(**self.user_conn_params)
                db_logger.info(f"Logged in as existing user '{new_user}' in PostgreSQL.")
            except psycopg2.OperationalError as e:
                db_logger.error(f"Failed to log in as user '{new_user}': {e}")
                raise
        except Exception as e:
            db_logger.error(f"An error occurred while creating user '{new_user}': {e}")
            raise

    def create_db(self, name: str) -> None:
        """Create a new PostgreSQL database with the given name using the current user."""
        if not self.conn:
            raise Exception("Not connected as a user. Please create a user and log in first.")

        try:
            # The current user must have the CREATEDB privilege
            with self.conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE {psycopg2.extensions.quote_ident(name, self.conn)};")
                db_logger.info(f"Database '{name}' created by user '{self.user}'.")
        except psycopg2.errors.InsufficientPrivilege:
            db_logger.error(f"User '{self.user}' does not have permission to create a database.")
            raise
        except psycopg2.errors.DuplicateDatabase:
            db_logger.warning(f"Database '{name}' already exists.")
        except Exception as e:
            db_logger.error(f"An error occurred while creating database '{name}': {e}")
            raise

class SQLite(AbstractDB):
    def __init__(self, db_file='mydatabase.sqlite3'):
        self.db_file = db_file
        self.conn = None
        self.user = None  # Simulated user
        self.password = None  # Simulated password

    def create_user(self, username, password):
        """
        Simulate user creation in SQLite by storing the username and password.
        Since SQLite doesn't support user accounts natively.
        """
        self.user = username
        self.password = password
        db_logger.info(f"Simulated user '{username}' with password in SQLite.")

        # Connect to the SQLite database
        try:
            self.conn = sqlite3.connect(self.db_file)
            db_logger.info(f"Connected to SQLite database '{self.db_file}' as user '{username}'.")
        except sqlite3.Error as e:
            db_logger.error(f"Failed to connect to SQLite database '{self.db_file}': {e}")
            raise

    def create_db(self, name: str) -> None:
        """
        In SQLite, the database is the file itself. To simulate creating a database,
        we'll create a new SQLite file with the given name.
        """
        if not self.user:
            raise Exception("No user is logged in. Please create a user first.")

        try:
            db_file = f"{name}.sqlite3"
            self.conn = sqlite3.connect(db_file)
            self.db_file = db_file
            db_logger.info(f"Database '{db_file}' created by user '{self.user}' in SQLite.")
        except sqlite3.Error as e:
            db_logger.error(f"An error occurred while creating SQLite database '{name}': {e}")
            raise
