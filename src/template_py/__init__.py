from template_py.logger import logger


def hello() -> None:
    logger.info("Hello Logger!")


def add(x: int, y: int) -> int:
    return x + y
