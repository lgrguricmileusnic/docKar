import socket
import sys
import struct

# CAN_FRAME_HEADER_STRUCT = struct.Struct("=IBB2x")

# can_id = 0x123
# flags = 0
# max_len = 8
# data = bytes("AAAAAAAA", "ascii").ljust(max_len, b"\x00")
# result = CAN_FRAME_HEADER_STRUCT.pack(can_id, 8, flags) + data

# print(result.hex())

frame = 0x123.to_bytes(length=4, signed=False, byteorder=sys.byteorder) + 0x8.to_bytes() + 0x0.to_bytes(3, signed=False) + bytes("ABCDEFGH", "ascii").ljust(8, b"\x00")
print(frame.hex())
s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.bind(('vcan0', ))

print(s.send(frame))
