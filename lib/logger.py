""""""
import logging

class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    green = "\x1b[32;20m"
    black = "\x1b[30;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        #logging.DEBUG: green + format + reset,
        logging.DEBUG: black + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

class Logger:
    def __init__(self, name: str = 'logger', level: int = logging.WARN):
        logging.basicConfig()
        self._name = name
        self._level = level
        self._logger = logging.getLogger(name)
        #self._logger = logging.getLogger(__name__)
        self._logger = logging.getLogger(name)
        self._logger.propagate = False
        self._handler = logging.StreamHandler()

        self.configure()

    def configure(self):
        #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self._handler.setFormatter(CustomFormatter())
        self._logger.handlers = [self._handler]
        self._logger.setLevel(self._level)
        logging.basicConfig(level=self._level, format='%(message)s')

    def debug(self, msg: str, *args, **kwargs): self._logger.debug(msg, *args, **kwargs)
    def info(self, msg: str, *args, **kwargs): self._logger.info(msg, *args, **kwargs)
    def warning(self, msg: str, *args, **kwargs): self._logger.warning(msg, *args, **kwargs)
    def warn(self, msg: str, *args, **kwargs): self._logger.warning(msg, *args, **kwargs)
    def error(self, msg: str, *args, **kwargs): self._logger.error(msg, *args, **kwargs)

