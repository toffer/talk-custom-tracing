import datetime
import logging

from utc import UTC


logging.basicConfig(format='%(message)s', filename='logs/har.log', level=logging.DEBUG)
har_logger = logging.getLogger('har_logger')


start_times = {}

class HARTracer(object):

    def __init__(self):
        self.start_times = {}

    def trace(self, frame, event, arg):
        if event == 'call':
            return self.handle_call(frame, event, arg)
        elif event == 'return':
            return self.handle_return(frame,event, arg)
        else:
            return self.trace

    @staticmethod
    def duration_in_milliseconds(start_time, end_time):
        delta = end_time - start_time
        milliseconds = (delta.seconds * 1000) + (delta.microseconds / 1000)
        return milliseconds

    def handle_call(self, frame, event, arg):
        self.start_times[frame] = datetime.datetime.now(UTC())
        return self.trace

    def handle_return(self, frame, event, arg):
        co = frame.f_code
        func_name = co.co_name

        start_time = self.start_times[frame]
        del self.start_times[frame]

        end_time = datetime.datetime.now(UTC())
        duration = self.duration_in_milliseconds(start_time, end_time)

        har_logger.debug('%s,%s,%f' %
                (func_name, start_time.timestamp(), duration))

        return None



def trace_call_2(frame, event, arg):

    co = frame.f_code
    func_name = co.co_name

    if event == 'call':
        start_times[frame] = datetime.datetime.now(UTC())
        print(func_name, start_times)
        return trace_call_2

    elif event == 'return':
        print('return', start_times)
        start_time = start_times[frame]
        del start_times[frame]

        end_time = datetime.datetime.now(UTC())
        duration_delta = end_time - start_time
        duration_in_milliseconds = (duration_delta.seconds * 1000) + (duration_delta.microseconds / 1000)

        har_logger.debug('%s,%s,%f' %
                (func_name, start_time.timestamp(), duration_in_milliseconds))



def trace_call(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    parent_frame = frame.f_back

    if event == 'call':

        def return_tracer(frame, event, arg):
            return trace_return(frame, event, arg)

        return_tracer._start_time = datetime.datetime.now(UTC())
        return return_tracer
    else:
        print('NOT A CALL')
        return None


def trace_return(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    parent_frame = frame.f_back

    # Get start_time
    start_time = frame.f_trace._start_time
    end_time = datetime.datetime.now(UTC())
    duration_delta = end_time - start_time
    duration_in_milliseconds = (duration_delta.seconds * 1000) + (duration_delta.microseconds / 1000)

    if event == 'return':
        har_logger.debug('%s,%s,%f' %
                (func_name, start_time.timestamp(), duration_in_milliseconds))
    elif event == 'call':
        print('CALL EVENT IN RETURN TRACER')
    return None
