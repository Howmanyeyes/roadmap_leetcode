"""Classes for db interactions"""
import abc
import psycopg2

from Andrey.PostgreSQL.consts import db_logger

class AbstractDB(abc.ABC):
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
            db_logger.info("Connected to PostgreSQL.")
            return True
        except psycopg2.OperationalError as e:
            db_logger.info("PostgreSQL is not available. Falling back to SQLite.")
            return False
    
    @abc.abstractmethod
    def connect_to_db(self):
        pass

class SQLite(AbstractDB):
    pass

class PostgreSQL(AbstractDB):
    pass