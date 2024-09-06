import Evtx.Evtx as evtx
import xml.etree.ElementTree as ET

def parse_evtx(file_path):
    cnt = 0
    with evtx.Evtx(file_path) as log:
        for record in log.records():
            xml_str = record.xml()
            xml = ET.fromstring(xml_str)
            cnt += 1
            print(ET.tostring(xml, encoding='utf8').decode('utf8'))
    print(cnt)

parse_evtx('security-logs.evtx')
