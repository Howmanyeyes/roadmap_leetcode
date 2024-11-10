import pytest
import logging
import threading
from unittest.mock import patch, MagicMock
from io import StringIO
from contextlib import redirect_stdout
import os

# Import the make_logger function and HTTPLogHandler class
from Andrey.PostgreSQL.utils import make_logger, HTTPLogHandler

TEST_LOG_DIR = 'test_log'

import logging
import time

class DelayedHandler(logging.Handler):
    def __init__(self, delay=1.0):
        super().__init__()
        self.delay = delay  # Delay in seconds
        self.processing_started = threading.Event()
        self.processing_finished = threading.Event()

    def emit(self, record):
        # Signal that processing has started
        self.processing_started.set()
        time.sleep(self.delay)
        # Signal that processing has finished
        self.processing_finished.set()
        # For testing purposes, we won't do any actual logging

def test_bad_logger_init():
    # Test case for bad input
    with pytest.raises(Exception):
        logger = make_logger()

def test_stupid_logger_init():
    with pytest.raises(Exception):
        logger = make_logger(write_to_console=False, name='sss')

def test_async_console_logging():
    # Redirect stdout to capture console output
    with StringIO() as buf, redirect_stdout(buf):
        logger = make_logger(
            name='test_logger',
            write_to_console=True
        )
        logger.info('Test message for console')

        # Stop the listener to ensure all logs are processed
        # if hasattr(logger, 'listener'):
        #     logger.listener.stop()

        output = buf.getvalue()

    # Assert that the message was logged to console
    assert 'Test message for' in output


def test_async_file_logging():
    path_to_file = [TEST_LOG_DIR]


    logger = make_logger(
        name='test_logger',
        write_to_console=False,
        write_to_file=True,
        path_to_file=path_to_file,
        write_to_url=False,
        async_logging=True,
        level='INFO'
    )
    log_file_path = os.path.join(os.getcwd(), *path_to_file, 'test_logger.log')

    logger.info('Test message for file')

    # Stop the listener
    if hasattr(logger, 'listener'):
        logger.listener.stop()

    # Read the log file content
    assert os.path.exists(log_file_path), f"Log file {log_file_path} was not created."

    with open(log_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Assert that the message was logged to the file
    assert 'Test message for file' in content

def test_async_listener_start_stop():
    logger = make_logger(
        name='test_logger',
        write_to_console=True,
        write_to_file=False,
        write_to_url=False,
        async_logging=True,
        level='INFO'
    )

    # Assert that listener is running
    assert hasattr(logger, 'listener'), "Logger should have a 'listener' attribute."
    assert isinstance(logger.listener, logging.handlers.QueueListener), "'listener' should be a QueueListener instance."

    # Check that the listener's thread is alive
    listener_thread = logger.listener._thread
    assert listener_thread is not None, "Listener thread should not be None after starting."
    assert listener_thread.is_alive(), "Listener thread should be alive after starting."

    # Stop the listener
    logger.listener.stop()

    # After stopping, the listener's thread should be None or not alive
    listener_thread = logger.listener._thread
    assert listener_thread is None or not listener_thread.is_alive(), "Listener thread should be None or not alive after stopping."


def test_async_logging_parallel_execution():
    handler_delay = 15.0  # Delay in seconds

    # Create a logger with asynchronous logging
    async_logger = make_logger(
        name='async_logger',
        write_to_console=True,
        write_to_file=False,
        write_to_url=False,
        async_logging=True,
        level='INFO'
    )

    # Create the delayed handler and add it to the logger
    delayed_handler = DelayedHandler(delay=handler_delay)
    # async_logger.addHandler(delayed_handler)
    async_logger.listener.handlers = (delayed_handler)

    # Log a message
    start_time = time.time()
    async_logger.info('Test message for async logger')

    # Wait until the handler starts processing
    handler_started = delayed_handler.processing_started.wait(timeout=1.0)

    # Perform another action in the main thread
    main_thread_action_start = time.time()
    time.sleep(3.0)  # Simulate work in the main thread
    main_thread_action_end = time.time()

    # Stop the listener to clean up
    #if hasattr(async_logger, 'listener'):
    #    async_logger.listener.stop()

    # Check if the handler is still processing after main thread action
    handler_finished = delayed_handler.processing_finished.is_set()

    # Output the times for debugging
    tot_time = time.time() - start_time
    main_thread_time = main_thread_action_end - main_thread_action_start
    print(f"Total time elapsed: {tot_time:.2f} seconds")
    print(f"Main thread action duration: {main_thread_time:.2f} seconds")


    # Assert that the handler was still processing after the main thread action
    assert tot_time - main_thread_time < handler_delay, "Handler should still be processing after main thread action."
