import os
import logging
import sys
import time


logging.basicConfig(
        format='%(message)s',
        filename='logs/zipkin.log',
        filemode='w',
        level=logging.DEBUG
)
zipkin_logger = logging.getLogger('zipkin_logger')


def trace_call(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    parent_frame = frame.f_back

    # Generate new span_id
    span_id = os.urandom(8).hex()
    try:
        parent_span_id = parent_frame.f_trace._span_id
    except AttributeError:
        parent_span_id = ''

    if event == 'call':
        zipkin_logger.debug('%s,%s,%s,%f,%s' %
                (span_id, parent_span_id, func_name, time.time(), 'sr'))

        def return_tracer(frame, event, arg):
            return trace_return(frame, event, arg)

        return_tracer._span_id = span_id
        return return_tracer
    else:
        print('NOT A CALL')
        return None


def trace_return(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    parent_frame = frame.f_back

    # Get existing span_id
    span_id = frame.f_trace._span_id
    try:
        parent_span_id = parent_frame.f_trace._span_id
    except AttributeError:
        parent_span_id = ''

    if event == 'return':
        zipkin_logger.debug('%s,%s,%s,%f,%s' %
                (span_id, parent_span_id, func_name, time.time(), 'ss'))
    elif event == 'call':
        print('CALL EVENT IN RETURN TRACER')
    return None
