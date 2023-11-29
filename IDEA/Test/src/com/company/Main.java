
/*
 *   Author: Hoesch, Paul
 *   Datum: 2021.10.05
 */

package com.company;

import java.io.IOException;
import java.util.Random;

public class Main {

    public static void main(String[] args) throws java.io.IOException {

        final int UPPER_LIMIT = 100;
        char wh;
        do {
            int inputNumber = input();

            int randomNumber = random(UPPER_LIMIT);

            boolean isRandomNumberGreater = check(randomNumber, inputNumber);

            if (isRandomNumberGreater)
                write(inputNumber, randomNumber);

            System.out.println("Wiederholen mit J oder j!");
            wh = new java.util.Scanner(System.in).next().charAt(0);
        } while (wh == 'j' || wh == 'J');
    }

    public static int input() {
        var scan = new java.util.Scanner(System.in);
        int i;
        do {
            System.out.println("Bitte eine Zahl zwischen 0 und 100 eingeben:");
            i = scan.nextInt();
        } while (i > 100 || i < 0);
        return i;
    }

    public static int random(int UPPER_LIMIT) {
        var random = new Random();
        int generatedNumber = random.nextInt(UPPER_LIMIT + 1);
        if (generatedNumber % 2 == 1) {
            generatedNumber--;
        }
        System.out.println("Erzeugte Zufallszahl: " + generatedNumber);
        return generatedNumber;
    }

    public static boolean check(int randomNumber, int inputNumber) {
        boolean isRandomNumberGreater;
        if (randomNumber > inputNumber) {
            System.out.println("Die Zufallszahl ist größer als die eingegebene Zahl.");
            isRandomNumberGreater = true;
        } else {
            System.out.println("Die Zufallszahl ist nicht größer als die eingegebene Zahl!");
            isRandomNumberGreater = false;
        }
        return isRandomNumberGreater;
    }

    public static void write(int inputNumber, int randomNumber) throws IOException {
        var path = java.nio.file.Paths.get("TwoNumbers.txt");
        var writer = java.nio.file.Files.newBufferedWriter(path);
        writer.write("Eingabe: " + inputNumber + ", Zufall: " + randomNumber);
        writer.close();
    }
}