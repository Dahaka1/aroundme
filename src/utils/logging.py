import logging


_logger = None


def get_logger():
    global _logger

    if _logger is None:
        _logger = logging.getLogger()

    return _logger
