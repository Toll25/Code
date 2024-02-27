package org.example;

import java.util.*;

class VaultDoor3 {
    public static void main(String[] args) {

        int i;
        for (i = 0; i < 8; i++) {
            System.out.println(i);
        }
        System.out.println("End First");
        for (; i < 16; i++) {
            System.out.println(i);
        }
        System.out.println("End Second");

        for (; i < 32; i += 2) {
            System.out.println(i);
        }
        System.out.println("End Third");

        for (i = 31; i >= 17; i -= 2) {
            System.out.println(i);
        }
        System.out.println("End Forth");


        String encryptedPassword = "jU5t_a_sna_3lpm18g947_u_4_m9r54f";
        char[] password = new char[32];

        for (i = 17; i <= 31; i += 2) {
            password[i] = encryptedPassword.charAt(i);
        }

        for (i = 30; i >= 16; i -= 2) {
            password[i] = encryptedPassword.charAt(46 - i);
        }

        for (i = 15; i >= 8; i--) {
            password[i] = encryptedPassword.charAt(23 - i);
        }

        for (i = 7; i >= 0; i--) {
            password[i] = encryptedPassword.charAt(i);
        }

        System.out.println(new String(password));

    }
}
