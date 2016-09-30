def localtrace_trace(self, frame, why, arg):
    if why == "line":
        filename = frame.f_code.co_filename
        bname = os.path.basename(filename)
        lineno = frame.f_lineno
        line = linecache.getline(filename, lineno)

        print("%s(%d): %s" % (bname, lineno, line),
                end='')

    return self.localtrace
