
"""
Usage:
    Same as logging.basicConfig().
    Call clogging.basicConfig() will change the default Formatter
    of all root handlers.

Example:

    import clogging
    import logging

    clogging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info('something')

Compatibility:
    This module is compatible with python2 and python3.
"""

import logging

_COLOR = {
    'CRITICAL': '\033[1;31m',
    'ERROR':    '\033[1;35m',
    'WARNING':  '\033[1;33m',
    'INFO':     '\033[1;32m',
    'DEBUG':    '\033[1;36m',
    'END':      '\033[m',
}

DEFAULT_FORMAT = '%(levelname)-8s %(asctime)s %(filename)s:%(lineno)d| %(message)s'


class ColorfulFormatter(logging.Formatter):
    def format(self, record):
        s = super(ColorfulFormatter, self).format(record)
        if record.levelname in _COLOR:
            s = _COLOR[record.levelname] + s + _COLOR['END']
        return s


def basicConfig(**kwargs):
    if 'format' not in kwargs:
        kwargs['format'] = DEFAULT_FORMAT

    logging.basicConfig(**kwargs)

    colorful_formatter = ColorfulFormatter(fmt=kwargs['format'])
    root_logger = logging.getLogger()
    for hdlr in root_logger.handlers:
        hdlr.setFormatter(colorful_formatter)