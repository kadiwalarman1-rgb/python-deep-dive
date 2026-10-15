import logging
from pathlib import Path


class EcommerceLogger:
    def __init__(self, name="ecommerce", log_file="lab34_output/ecommerce.log"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        target = Path(log_file)
        target.parent.mkdir(parents=True, exist_ok=True)
        resolved = str(target.resolve())
        configured_files = {
            str(Path(handler.baseFilename).resolve())
            for handler in self.logger.handlers
            if isinstance(handler, logging.FileHandler)
        }
        if resolved not in configured_files:
            file_handler = logging.FileHandler(target, encoding="utf-8")
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            ))
            self.logger.addHandler(file_handler)
        if not any(type(handler) is logging.StreamHandler for handler in self.logger.handlers):
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
            self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)
