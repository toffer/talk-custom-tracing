class Span(object):

    def __init__(self, span_id, parent_id, trace_id, name,
            timestamp, debug=True):
        self.span_id = span_id
        self.parent_id = parent_id
        self.trace_id = trace_id
        self.name = name
        self.timestamp = timestamp
        self.debug = debug
        self.annotations = []

    def add_annotation(self, annotation):
        self.annotations.append(annotation)

    def asdict(self):
        d = {
            'id': self.span_id,
            'traceId': self.trace_id,
            'name': self.name,
            'timestamp': self.timestamp,
            'debug': self.debug,
            'annotations': [a.asdict() for a in self.annotations]
        }
        if self.parent_id:
            d['parentId'] = self.parent_id
        return d

    def __repr__(self):
        return ('<Span id=%s, parent_id=%s, trace_id=%s, name=%s, '
                'timestamp=%d, value=%s>' % (self.span_id, self.parent_id,
                self.trace_id, self.name, self.timestamp,
                self.annotations[0].value))


class Annotation(object):

    def __init__(self, endpoint, timestamp, value):
        self.endpoint = endpoint
        self.timestamp = timestamp
        self.value = value

    def asdict(self):
        return {
            'endpoint': self.endpoint.asdict(),
            'timestamp': self.timestamp,
            'value': self.value
        }


class Endpoint(object):

    def __init__(self, ipv4, port, service_name):
        self.ipv4 = ipv4
        self.port = port
        self.service_name = service_name

    def asdict(self):
        return {
            'ipv4': self.ipv4,
            'port': self.port,
            'serviceName': self.service_name
        }
