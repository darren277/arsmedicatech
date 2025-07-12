"""
Custom Logger with Colored Output
"""
import logging
from typing import Any


class CustomFormatter(logging.Formatter):
    """
    Custom formatter to add colors to log messages based on their severity level.
    """
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    green = "\x1b[32;20m"
    black = "\x1b[30;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        #logging.DEBUG: green + log_format + reset,
        logging.DEBUG: black + log_format + reset,
        logging.INFO: grey + log_format + reset,
        logging.WARNING: yellow + log_format + reset,
        logging.ERROR: red + log_format + reset,
        logging.CRITICAL: bold_red + log_format + reset
    }

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record with the appropriate color based on its level.
        :param record: logging.LogRecord
        :return: str
        """
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

class Logger:
    """
    Custom logger class that uses the standard logging library with a custom formatter.
    """
    def __init__(self, name: str = 'logger', level: int = logging.WARN) -> None:
        """
        Initialize the logger with a name and logging level.
        :param name: The name of the logger.
        :param level: The logging level (default is logging.WARN).
        :return: None
        """
        logging.basicConfig()
        self._name = name
        self._level = level
        self._logger = logging.getLogger(name)
        #self._logger = logging.getLogger(__name__)
        self._logger = logging.getLogger(name)
        self._logger.propagate = False
        self._handler = logging.StreamHandler()

        self.configure()

    def configure(self) -> None:
        """
        Configure the logger with a custom formatter and set the logging level.
        :return: None
        """
        #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self._handler.setFormatter(CustomFormatter())
        self._logger.handlers = [self._handler]
        self._logger.setLevel(self._level)
        logging.basicConfig(level=self._level, format='%(message)s')

    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """
        Log a debug message.
        :param msg: The message to log.
        :param args: Additional arguments to format the message.
        :param kwargs: Additional keyword arguments for logging.
        :return: None
        """
        self._logger.debug(msg, *args, **kwargs)

    def info(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """
        Log an info message.
        :param msg: The message to log.
        :param args: Additional arguments to format the message.
        :param kwargs: Additional keyword arguments for logging.
        :return: None
        """
        self._logger.info(msg, *args, **kwargs)

    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """
        Log a warning message.
        :param msg: The message to log.
        :param args: Additional arguments to format the message.
        :param kwargs: Additional keyword arguments for logging.
        :return: None
        """
        self._logger.warning(msg, *args, **kwargs)

    def warn(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """
        Log a warning message.
        :param msg: The message to log.
        :param args: Additional arguments to format the message.
        :param kwargs: Additional keyword arguments for logging.
        :return: None
        """
        self._logger.warning(msg, *args, **kwargs)

    def error(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """
        Log an error message.
        :param msg: The message to log.
        :param args: Additional arguments to format the message.
        :param kwargs: Additional keyword arguments for logging.
        :return: None
        """
        self._logger.error(msg, *args, **kwargs)
