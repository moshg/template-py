import structlog
from structlog.typing import FilteringBoundLogger, Processor

from template_py.config import settings

# default value: https://www.structlog.org/en/25.4.0/getting-started.html#your-first-log-entry
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


structlog.configure(
    processors=_processors,
)


logger: FilteringBoundLogger = structlog.get_logger()
