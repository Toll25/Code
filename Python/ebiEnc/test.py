state1 = 14144
state2 = 14144
sbox = [0xb7e15162, 0xbf715880, 0x38b4da56, 0x324e7738, 0xbb1185eb]


def aes_round(round_):
    global state1
    global state2

    Tm = (state1 + (state2 >> 0x1f | ((state2 << 1) & 0xffffffff))) & 0xffffffff
    Tmp = state2 ^ (Tm >> 0x18 | ((Tm * 0x100) & 0xffffffff))
    t = sbox[round_ % 5]


    Tm = ((Tm ^ t) + (Tmp >> 0x11 | Tmp << 0xf)) & 0xffffffff
    Tmp = Tmp ^ (Tm >> 17 | ((Tm * 0x8000) & 0xffffffff))
    Tm = ((Tm ^ t) + Tmp) & 0xffffffff
    Tmp = Tmp ^ (Tm >> 31 | ((Tm * 2)) & 0xffffffff)

    Tm = ((Tm ^ t) + (Tmp >> 0x18 | ((Tmp << 8) & 0xffffffff))) & 0xffffffff


    state2 = Tmp ^ (Tm >> 16 | ((Tm * 0x10000) & 0xffffffff))
    state1 = t ^ Tm

def reverse_aes_round(round_):
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

print(state1)
print(state2)
aes_round(1)

print(state1)
print(state2)
reverse_aes_round(1)

print(state1)
print(state2)