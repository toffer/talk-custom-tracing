import linecache
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
        format='%(message)s',
        filename='logs/trace.log',
        filemode='w',
        level=logging.INFO
)

def filename_tracer(frame, event, arg):
    fname = frame.f_code.co_filename
    co_name = frame.f_code.co_name
    num = frame.f_lineno
    line = linecache.getline(fname, num)

    if event == 'call':
        logger.info("--- %s: %s", fname, co_name)
    elif event == 'line':
        logger.info("%s(%d): %s", fname, num, line)

    return filename_tracer
