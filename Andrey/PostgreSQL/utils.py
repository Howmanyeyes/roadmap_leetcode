"""Python file with different utilities helpfull for all projects."""
import logging
import os
import sys
import asyncio
import requests


class HTTPLogHandler(logging.Handler):
    """
    Dummy logging handler that sends log records to a specified HTTP URL.
    """
    def __init__(self, url, api_key=None, api_secret=None, username=None, password=None):
        super().__init__()
        self.url = url
        self.api_key = api_key
        self.api_secret = api_secret
        self.username = username
        self.password = password

    def emit(self, record):
        try:
            log_entry = self.format(record)

            headers = {'Content-Type': 'application/json'}
            data = {'log': log_entry}

            # Add authentication if provided
            auth = None
            if self.username and self.password:
                auth = (self.username, self.password)
            elif self.api_key and self.api_secret:
                headers['API_KEY'] = self.api_key
                headers['API_SECRET'] = self.api_secret

            # Send the log entry to the specified URL
            response = requests.post(self.url, json=data, headers=headers, auth=auth)
            response.raise_for_status()

        except Exception:
            self.handleError(record)


def make_logger(name: str,
                encoding: str = 'utf-8',
                write_to_console: bool = True,
                write_to_file: bool = False,
                write_to_url: bool = False,
                path_to_file: list = None,
                url: str = None,
                method: str = None,
                async_logging: bool = False,
                format: str = '%(asctime)s / %(name)s / %(levelname)s / %(message)s',
                datefmt: str = '%d-%m-Y% %H:%M:%S',
                **kwargs
                ) -> logging.Logger:
    """
    Function to make your perfect logger!\n
    - `name`, `write_to_console` and `encoding` are self-explanatory\n
    - `path_to_file` must be a list that contains directions to your desired folder starting from 
    palcement of this module\n
    - `write_to_url` allows you to write asyncly or not to urls, to use it `url` must be specified
    , but API or auth credentials are not nessesary
    - Right now `write_to_url` is not working, this is because it is impossible to make correct
    format for every web app that exists (some require signatures abtanable through API, others
    make you include username and password within body of responce). So that's why in addition to
    supplying link you must also provide name of the logging handler and all nessesary `**kwargs`
    for that handler to function.
    """

    url_handlers = {
        "HTTPLogHandler": HTTPLogHandler
    }

    logger = logging.getLogger(name=name)
    logger.setLevel(logging.INFO)
    if logger.hasHandlers():
        logger.handlers.clear()
    
    formatter = logging.Formatter(fmt=format, datefmt=datefmt)

    if not write_to_console and not write_to_file and not write_to_url:
        raise ValueError("At least one of write_to_console, write_to_file, or write_to_url must be True.")

    if async_logging:
        pass
    else:
        if write_to_console:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        if write_to_file:
            if path_to_file is not None:
                file_path = os.path.join(os.path.dirname(__file__), *path_to_file)
                os.makedirs(file_path, exist_ok=True)
                log_file = os.path.join(file_path, f'{name}.log')
                file_handler = logging.FileHandler(filename=log_file, encoding=encoding)
            else:
                file_path = os.path.dirname(__file__)
                log_file = os.path.join(file_path, f'{name}.log')
                file_handler = logging.FileHandler(filename=log_file, encoding=encoding)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        if write_to_url:
            if url is None or url_handlers.get(method, None) is None:
                raise ValueError("url and method must be specified when write_to_url is True.")
            else:
                kwargs['url'] = url
                url_handler = url_handlers[method](**kwargs)
                url_handler.setFormatter(formatter)
                logger.addHandler(url_handler)
