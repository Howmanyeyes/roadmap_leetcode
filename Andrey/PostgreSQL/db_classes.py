"""Classes for db interactions"""
from abc import ABC
import psycopg2

class AbstractDB(ABC):
    """Abstract class for db, it will be used only to determine if PostgreSQL exists"""
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
            print("Connected to PostgreSQL.")
            return True
        except psycopg2.OperationalError as e:
            print("PostgreSQL is not available. Falling back to SQLite.")
            return False


class SQLite():
    pass


class PostgreSQL():
    pass