import logging


def _logger():
    test_logger = logging.getLogger("JenkinsLogger")
    stream_handler = logging.StreamHandler()
    stream_format = logging.Formatter(f'[%(asctime)s][%(levelname)s][%(filename)s:%(funcName)s:%(lineno)s] %(message)s')
    stream_handler.setFormatter(stream_format)
    test_logger.addHandler(stream_handler)
    test_logger.setLevel(logging.INFO)
    return test_logger


logger = _logger()
