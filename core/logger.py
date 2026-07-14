from __future__ import annotations

import logging
from pathlib import Path

from config import LOG_DIR, DEBUG


class Logger:

    def __init__(self):

        LOG_DIR.mkdir(exist_ok=True)

        self.logger = logging.getLogger("FRISK")

        if self.logger.handlers:
            return

        level = logging.DEBUG if DEBUG else logging.INFO

        self.logger.setLevel(level)

        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s",
            "%H:%M:%S"
        )

        file_handler = logging.FileHandler(
            LOG_DIR / "frisk.log",
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message: str):

        self.logger.info(message)

    def warning(self, message: str):

        self.logger.warning(message)

    def error(self, message: str):

        self.logger.error(message)

    def debug(self, message: str):

        self.logger.debug(message)