"""Module with inicialization of all nessesary consts"""

from Andrey.PostgreSQL.utils import make_logger

db_logger = make_logger(name='db_logger', write_to_file=True,
                        path_to_file=['Andrey', 'PostgreSQL', 'logs'], write_to_console=True)