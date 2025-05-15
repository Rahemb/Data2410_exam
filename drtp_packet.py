# drtp_packet.py

import struct

# Constants for flags
FLAG_SYN = 0b1000
FLAG_ACK = 0b0100
FLAG_FIN = 0b0010
FLAG_RST = 0b0001

# Construct a DRTP packet
def make_packet(seq, ack, flags, window, data=b''):
    header = struct.pack("!HHHH", seq, ack, flags, window)
    return header + data

# Parse a DRTP packet into its components
def parse_packet(packet):
    header = packet[:8]
    data = packet[8:]
    seq, ack, flags, window = struct.unpack("!HHHH", header)
    return seq, ack, flags, window, data

