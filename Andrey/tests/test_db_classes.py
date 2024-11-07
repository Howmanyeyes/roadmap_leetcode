# import pytest
from unittest.mock import patch, MagicMock
from psycopg2 import OperationalError

# Import the AbstractDB class from your module
from Andrey.PostgreSQL.db_classes import AbstractDB

def test_search_for_sql_success():
    with patch('psycopg2.connect') as mock_connect:
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        result = AbstractDB.search_for_sql()
        assert result == True
        mock_connect.assert_called_once()

def test_search_for_sql_failure():
    with patch('psycopg2.connect', side_effect=OperationalError("Test Error")):
        result = AbstractDB.search_for_sql()
        assert result == False
