package com.company;

import java.lang.reflect.Array;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        var scan = new java.util.Scanner(System.in);
        long temp, dec = 1;
        ArrayList<Long> bin = new ArrayList<Long>();

        System.out.println("Bitte eine Dezimalzahl eingeben");
        dec = scan.nextLong();

        temp = dec;

        while (temp != 0) {
            bin.add(temp % 2);
            temp = temp / 2;
        }
        for (long i : bin) {
            System.out.print(i);
        }
    }
}