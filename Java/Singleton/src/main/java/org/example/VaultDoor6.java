package org.example;

import java.util.*;

class VaultDoor6 {
    public static void main(String args[]) {
        byte[] passBytes = new byte[32];
        byte[] myBytes = {
                0x3b, 0x65, 0x21, 0xa, 0x38, 0x0, 0x36, 0x1d,
                0xa, 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa,
                0x21, 0x1d, 0x61, 0x3b, 0xa, 0x2d, 0x65, 0x27,
                0xa, 0x6c, 0x61, 0x6d, 0x37, 0x6d, 0x6d, 0x6d,
        };
        for (int i = 0; i < 32; i++) {
            passBytes[i] = (byte) (myBytes[i]^0x55);
        }

        System.out.println(new String(passBytes));
    }

    public boolean checkPassword(String password) {



        return true;
    }
}

