__all__: list[str] = []

import logging

from torch.distributed.logging_handlers import _log_handlers


DCP_LOGGER_NAME = "dcp_logger"

_log_handlers.update(
    {
        DCP_LOGGER_NAME: logging.NullHandler(),
    }
)
