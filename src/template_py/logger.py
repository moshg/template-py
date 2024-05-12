import logging

import structlog
from structlog.typing import FilteringBoundLogger

from template_py.config import log_format

_shared_processors = [
    structlog.contextvars.merge_contextvars,
    structlog.processors.add_log_level,
    # If the "stack_info" key in the event dict is true, remove it and
    # render the current stack trace in the "stack" key.
    structlog.processors.StackInfoRenderer(),
]

_console_processors = _shared_processors + [
    # ConsoleRenderer handles the exc_info event dict key itself.
    structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", utc=False),
    structlog.dev.ConsoleRenderer(),
]

_json_processors = _shared_processors + [
    # Delegate timestamps to monitoring service.
    # If the "exc_info" key in the event dict is either true or a
    # sys.exc_info() tuple, remove "exc_info" and render the exception
    # with traceback into the "exception" key.
    structlog.processors.format_exc_info,
    structlog.processors.JSONRenderer(),
]


structlog.configure(
    processors=_json_processors if log_format == "json" else _console_processors,
    # These are the default values.
    # We specify them explicitly against changes due to version upgrades.
    wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
    logger_factory=structlog.PrintLoggerFactory(),
)

logger: FilteringBoundLogger = structlog.get_logger()
