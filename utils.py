""""""
from settings import logger


import ssl
import socket
from pprint import pprint
from datetime import datetime

def fetch_cert(hostname, port=443):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port), timeout=5) as sock:
        try:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                return cert
        except ssl.SSLError as e:
            print(f"SSL error: {e}")
            return None

def parse_cert(cert):
    if not cert:
        logger.debug("❌ No certificate found or unable to fetch.")
        return

    logger.debug("\n📄 Subject:")
    pprint(cert.get('subject'))

    logger.debug("\n🏢 Issuer:")
    pprint(cert.get('issuer'))

    logger.debug("\n📅 Validity Period:")
    print(f"  Not Before: {cert.get('notBefore')}")
    print(f"  Not After : {cert.get('notAfter')}")

    logger.debug("\n🌐 Subject Alt Names:")
    pprint(cert.get('subjectAltName'))

    # Expiry check
    not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
    days_left = (not_after - datetime.utcnow()).days
    print(f"\n✅ Expires in: {days_left} days")

    if days_left < 0:
        logger.debug("❌ Certificate has expired!")
    elif days_left < 10:
        logger.debug("⚠️ Certificate is about to expire!")

if __name__ == "__main__":
    domain = "demo.arsmedicatech.com"
    cert = fetch_cert(domain)
    parse_cert(cert)


quit(45)


sql_query = """
CREATE TABLE `formAR` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `demographic_no` int(10) NOT NULL DEFAULT '0',
  `provider_no` varchar(6) DEFAULT NULL,
  `formCreated` date DEFAULT NULL,
  `formEdited` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `c_lastVisited` char(3) DEFAULT NULL,
  `c_pName` varchar(60) DEFAULT NULL,
  `c_address` varchar(80) DEFAULT NULL,
  `pg1_dateOfBirth` date DEFAULT NULL,
  `pg1_age` char(2) DEFAULT NULL,
  `pg1_msSingle` tinyint(1) DEFAULT NULL,
  `pg1_msCommonLaw` tinyint(1) DEFAULT NULL,
  `pg1_msMarried` tinyint(1) DEFAULT NULL,
  `pg1_eduLevel` varchar(25) DEFAULT NULL,
  `pg2_date1` date DEFAULT NULL,
  `pg2_gest1` varchar(6) DEFAULT NULL,
  `pg2_ht1` varchar(6) DEFAULT NULL,
  `pg2_wt1` varchar(6) DEFAULT NULL,
  `pg2_presn1` varchar(6) DEFAULT NULL,
  `pg3_presn34` varchar(6) DEFAULT NULL,
  `pg3_FHR34` varchar(6) DEFAULT NULL,
  `pg3_urinePr34` char(3) DEFAULT NULL,
  `pg3_urineGl34` char(3) DEFAULT NULL,
  `pg3_BP34` varchar(8) DEFAULT NULL,
  `pg3_comments34` text DEFAULT NULL,
  `pg3_cig34` char(3) DEFAULT NULL,
  `ar2_obstetrician` tinyint(1) DEFAULT NULL,
  `ar2_pediatrician` tinyint(1) DEFAULT NULL,
  `ar2_anesthesiologist` tinyint(1) DEFAULT NULL,
  `ar2_socialWorker` tinyint(1) DEFAULT NULL,
  `ar2_dietician` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB
  ROW_FORMAT=DYNAMIC;
"""


def calculate_row_size(sql_string: str):
    row_size = 0
    for line in sql_string.split('\n'):
        print(line)
        line = line.lstrip().rstrip()
        if line.startswith('CREATE TABLE'):
            logger.debug("CONTINUING:", line)
            continue
        elif line.startswith('PRIMARY KEY'):
            logger.debug("BREAKING:", line)
            break
        elif line == '':
            logger.debug("CONTINUING:", line)
            continue
        x = line.split(' ')
        try:
            field_type = x[1].lstrip().rstrip()
        except:
            print("Error:", line)
            continue

        if field_type.startswith('varchar'):
            row_size += int(field_type.split('(')[1].split(')')[0]) * 4
        elif field_type.startswith('char'):
            row_size += int(field_type.split('(')[1].split(')')[0])
        elif field_type.startswith('int'):
            row_size += 4
        elif field_type.startswith('bigint'):
            row_size += 8
        elif field_type.startswith('tinyint'):
            row_size += 1
        elif field_type.startswith('date'):
            row_size += 3
        elif field_type.startswith('timestamp'):
            row_size += 4
        elif field_type.startswith('text'):
            row_size += 20
        else:
            print("Unknown field type:", field_type)
            print(line)
            if '`ID` INT NOT NULL' in line:
                row_size += 4
            else:
                raise Exception("Unknown field type")
    return row_size


print(calculate_row_size(sql_query))  # 202

start_line = 521
end_line = 694

file_path = 'emr/oscar/migrations/initcaisi.sql'

with open(file_path, 'r') as f:
    sql_lines = f.readlines()

    s = ""

    for i, line in enumerate(sql_lines):
        if i == start_line:
            s += line
        elif i > start_line and i < end_line:
            s += line
        elif i == end_line:
            s += line
            break


print(calculate_row_size(s))  # 202
