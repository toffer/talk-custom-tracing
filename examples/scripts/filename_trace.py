import linecache

def filename_tracer(frame, event, arg):
    fname = frame.f_code.co_filename
    co_name = frame.f_code.co_name
    lineno = frame.f_lineno
    line = linecache.getline(fname, lineno)

    if event == "call":
        print("--- %s: %s" % (fname, co_name))
    else:
        print("%s(%d): %s" % (fname, lineno, line))

    return filename_tracer
