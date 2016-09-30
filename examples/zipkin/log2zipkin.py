import binascii
import csv
import json
import os
import requests
import sys

from zipkin import Annotation, Endpoint, Span


DEFAULT_TRACE_ID = binascii.hexlify(os.urandom(8)).decode('ascii')
DEFAULT_ENDPOINT = Endpoint(
        ipv4='127.0.0.1',
        port=8888,
        service_name='simple_service'
)


def read_log(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            parsed = (row[0], row[1], row[2], float(row[3]), row[4])
            yield parsed


def make_span(span_id, parent_id, func_name, timestamp, annotation_value,
        endpoint=DEFAULT_ENDPOINT, debug=True):

    micro_timestamp = timestamp * (10 ** 6)

    span = Span(
            span_id=span_id,
            parent_id=parent_id,
            trace_id=DEFAULT_TRACE_ID,
            name=func_name,
            timestamp=micro_timestamp,
            debug=debug
    )

    annotation = Annotation(
            endpoint=DEFAULT_ENDPOINT,
            timestamp=micro_timestamp,
            value = annotation_value
    )

    span.add_annotation(annotation)
    return span


def send_span(span):
    url = 'http://192.168.99.100:9411/api/v1/spans'
    payload = [span.asdict()]
    resp = requests.post(url, json=payload)
    print(resp)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        filename = sys.argv[1]
    except:
        return 1

    for line in read_log(filename):
        span = make_span(*line)
        send_span(span)
        print(span)


if __name__ == '__main__':
    sys.exit(main())
