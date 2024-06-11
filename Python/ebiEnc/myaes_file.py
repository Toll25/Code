state1 = 0
state2 = 0

roundkeys = [0x00022312, 0x005fa32b, 0x005ac810]

sbox = [0xb7e15162, 0xbf715880, 0x38b4da56, 0x324e7738, 0xbb1185eb]


def aes_add_round_key(round_):
    global state1
    global state2
    state1 = state1 ^ roundkeys[(round_ & 1)] ^ round_
    state2 = state2 ^ roundkeys[(round_ & 1) + 1]


def aes_round(round_):
    global state1
    global state2
    Tm = (state1 + (state2 >> 0x1f | ((state2 << 1) & 0xffffffff))) & 0xffffffff;
    Tmp = state2 ^ (Tm >> 0x18 | ((Tm * 0x100) & 0xffffffff));
    t = sbox[round_ % 5]
    Tm = ((Tm ^ t) + (Tmp >> 0x11 | Tmp << 0xf)) & 0xffffffff;
    Tmp = Tmp ^ (Tm >> 17 | ((Tm * 0x8000) & 0xffffffff));
    Tm = ((Tm ^ t) + Tmp) & 0xffffffff;
    Tmp = Tmp ^ (Tm >> 31 | ((Tm * 2)) & 0xffffffff);
    Tm = ((Tm ^ t) + (Tmp >> 0x18 | ((Tmp << 8) & 0xffffffff))) & 0xffffffff;
    state2 = Tmp ^ (Tm >> 16 | ((Tm * 0x10000) & 0xffffffff));
    state1 = t ^ Tm;


def aes_undo_round(round_):
    global state1
    global state2
    t = sbox[round_ % 5]
    Tm = state1 ^ t
    Tmp = state2 ^ (Tm >> 16 | ((Tm << 16) & 0xffffffff))
    Tm = ((Tm - (Tmp >> 0x18 | ((Tmp << 8) & 0xffffffff)) + 0x100000000) & 0xffffffff) ^ t
    Tmp = Tmp ^ (Tm >> 31 | ((Tm * 2) & 0xffffffff))
    Tm = ((Tm - Tmp + + 0x100000000) & 0xffffffff) ^ t
    Tmp = Tmp ^ (Tm >> 17 | ((Tm * 0x8000) & 0xffffffff))
    Tm = ((Tm - (Tmp >> 0x11 | Tmp << 0xf) + 0x100000000) & 0xffffffff) ^t

    state2 = Tmp ^ (Tm >> 0x18 | ((Tm << 8) & 0xffffffff))
    state1 = (Tm - (state2 >> 0x1f | ((state2 << 1) & 0xffffffff)) + 0x100000000) & 0xffffffff


def aes(input1, input2):
    global state1
    global state2

    state1 = state1 ^ input1
    state2 = state2 ^ input2

    for i in range(10):
        #print(f"round {i}")
        aes_add_round_key(i)
        #print(f"{hex(state1)} {hex(state2)}")
        aes_round(i)
        #print(f"{hex(state1)} {hex(state2)}")

    #print(f"round final")
    aes_add_round_key(0)
    print(f"{le_hex(state1)}{le_hex(state2)}", end='')


def le_hex(intval):
    hex_string = format(intval, '08x')
    swapped_hex_string = ''.join(reversed([hex_string[i:i + 2] for i in range(0, len(hex_string), 2)]))
    return swapped_hex_string


import sys
import struct

with open(sys.argv[1], 'rb') as file:
    while True:
        uint_bytes = file.read(8)

        if not uint_bytes:
            break

        uint1, uint2 = struct.unpack('<II', uint_bytes)
        aes(uint1, uint2)
