import logging
from typing import assert_never

import structlog
from structlog.typing import FilteringBoundLogger, Processor

from template_py.config import settings

_shared_processors: list[Processor] = [
    structlog.contextvars.merge_contextvars,
    structlog.processors.add_log_level,
    # If the "stack_info" key in the event dict is true, remove it and
    # render the current stack trace in the "stack" key.
    structlog.processors.StackInfoRenderer(),
]

_console_processors: list[Processor] = _shared_processors + [
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

match settings.log_format:
    case "json":
        _processors = _json_processors
    case "console":
        _processors = _console_processors
    case _:
        assert_never(settings.log_format)


structlog.configure(
    processors=_processors,
    # These are the default values.
    # We specify them explicitly against changes due to version upgrades.
    wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
    logger_factory=structlog.PrintLoggerFactory(),
)

logger: FilteringBoundLogger = structlog.get_logger()
