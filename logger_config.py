import logging


def configure_logging():
    logging.basicConfig(
        filename="application.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        encoding="utf-8",
    )