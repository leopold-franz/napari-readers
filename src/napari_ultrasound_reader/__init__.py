from logging import config

log_config = {
    "version": 1,
    "loggers": {
        "follicle_tracker": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
        "root": {"level": "DEBUG", "handlers": ["null"]},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "null": {"class": "logging.NullHandler"},
    },
    "formatters": {
        "simple": {
            "format": "%(levelname)s - %(asctime)s - %(name)s - %(message)s"
        }
    },
}

config.dictConfig(log_config)
