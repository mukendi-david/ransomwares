# from scapy.all import rdpcap, IP
# import imaplib
# import email
# from email.header import decode_header
import shutil
import os
from datetime import datetime
from faker import Faker
import json

fake = Faker()


def generate_traffic_data(num_entries=50):
    traffic_data = []
    for i in range(1, num_entries + 1):
        traffic_data.append({
            "id": i,
            "source_ip": fake.ipv4(),
            "destination_ip": fake.ipv4(),
            "protocol": fake.random_element(elements=("TCP", "UDP", "ICMP")),
            "length": fake.random_int(min=40, max=1500),
            "info": fake.sentence()
        })
    return traffic_data


traffic_data = generate_traffic_data()
with open("C:\\Users\\admin\\Documents\\Memoire_L2\\ransomwares\\detection_ransomware\\templates\\json\\traffic_data.json", 'w') as f:
    json.dump(traffic_data, f, indent=4)


def generate_email_data(num_entries=50):
    email_data = []
    for i in range(1, num_entries + 1):
        email_data.append({
            "id": i,
            "sender": fake.email(),
            "subject": fake.sentence(),
            "content": fake.paragraph(),
            "date": fake.date_time_this_year().isoformat()
        })
    return email_data


email_data = generate_email_data()
with open("C:\\Users\\admin\\Documents\\Memoire_L2\\ransomwares\\detection_ransomware\\templates\\json\\email_data.json", 'w') as f:
    json.dump(email_data, f, indent=4)


def create_backup():
    backup_dir = "C:\\Users\\admin\\Documents\\Memoire_L2\\ransomwares\\files_ransomware"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_file = os.path.join(backup_dir, f"backup_{
                               datetime.now().strftime('%Y%m%d%H%M%S')}.zip")
    shutil.make_archive(backup_file.replace('.zip', ''), 'zip', backup_dir)
    return backup_file


# def parse_pcap(file_path):
#     packets = rdpcap(file_path)
#     parsed_packets = []
#     for pkt in packets:
#         if IP in pkt:
#             parsed_packets.append({
#                 'source_ip': pkt[IP].src,
#                 'destination_ip': pkt[IP].dst,
#                 'protocol': pkt[IP].proto,
#                 'length': len(pkt),
#                 'info': pkt.summary()
#             })
#     return parsed_packets


# def fetch_emails(username, password, server='imap.example.com'):
#     mail = imaplib.IMAP4_SSL(server)
#     mail.login(username, password)
#     mail.select("inbox")

#     result, data = mail.search(None, "ALL")
#     email_ids = data[0].split()

#     emails = []
#     for email_id in email_ids:
#         result, msg_data = mail.fetch(email_id, "(RFC822)")
#         raw_email = msg_data[0][1]
#         msg = email.message_from_bytes(raw_email)
#         emails.append({
#             'sender': msg['From'],
#             'subject': decode_header(msg['Subject'])[0][0],
#             'content': msg.get_payload()
#         })

#     mail.logout()
#     return emails
