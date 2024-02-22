from xml.sax.xmlreader import InputSource
from xml.sax.expatreader import create_parser
from xml.sax.handler import feature_external_ges

class TestEntityRecorder:
    def __init__(self):
        self.entities = []

    def resolveEntity(self, publicId, systemId):
        self.entities.append((publicId, systemId))
        source = InputSource()
        source.setPublicId(publicId)
        source.setSystemId(systemId)
        return source

parser = create_parser()
parser.setFeature(feature_external_ges, True)
resolver = TestEntityRecorder()
parser.setEntityResolver(resolver)

try:
    parser.feed(
        '<!DOCTYPE external SYSTEM "unsupported://non-existing">\n'
    )
except Exception:
    pass

import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

from test.support import os_helper
os_helper.fd_count()
