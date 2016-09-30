import logging
import os
import time


logging.basicConfig(
        format='%(message)s',
        filename='logs/zipkin.log',
        filemode='w',
        level=logging.DEBUG
)
zipkin_logger = logging.getLogger('zipkin_logger')

class ZipkinTracer(object):

    def __init__(self):
        self.span_ids = {}  # {frame: span_id}

    def __call__(self, frame, event, arg):
        if event == 'call':
            return self.trace_call(frame, event, arg)
        elif event == 'return':
            return self.trace_return(frame,event, arg)
        else:
            return self

    def parent_span_id(self, frame):
        parent = frame.f_back
        return self.span_ids.get(parent, '')

    def trace_call(self, frame, event, arg):
        current_id = os.urandom(8).hex()
        self.span_ids[frame] = current_id

        parent_id = self.parent_span_id(frame)
        func_name = frame.f_code.co_name
        zipkin_logger.debug('%s,%s,%s,%f,%s' % (
                current_id, parent_id, func_name,
                time.time(), 'sr'))

        return self

    def trace_return(self, frame, event, arg):
        current_id = self.span_ids[frame]
        parent_id = self.parent_span_id(frame)
        func_name = frame.f_code.co_name
        zipkin_logger.debug('%s,%s,%s,%f,%s' % (
                current_id, parent_id, func_name,
                time.time(), 'ss'))

        del self.span_ids[frame]
        return self
