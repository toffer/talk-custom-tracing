def system_tracer(frame, event, arg):
    if event == 'call':
        func_name = frame.f_code.co_name
        print('--- system_tracer: %r' % func_name)
    return local_tracer

def local_tracer(frame, event, arg):
    if event == 'line':
        lineno = frame.f_lineno
        print('local_tracer: lineno %d' % lineno)
    return local_tracer
