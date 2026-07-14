from core.logger import Logger


def test_logger_creation():

    logger = Logger()

    assert logger is not None