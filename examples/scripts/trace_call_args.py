def trace_call_args(frame, event, arg):
    if event == 'call':
        code = frame.f_code
        arg_count = code.co_argcount
        arg_names = code.co_varnames[:arg_count]

        print("%s: %s" % (code.co_filename, code.co_name))

        for name in arg_names:
            val = frame.f_locals[name]
            print('{:<4}{}: {}'.format(' ', name, val))

    return None


def trace_call_args_2(frame, event, arg):
    if event == 'call':
        code = frame.f_code

        print("%s: %s" % (code.co_filename, code.co_name))

        for name in frame.f_locals:
            val = frame.f_locals[name]
            print('{:<4}{:<7}: {}'.format(' ', name, val))

    return None

