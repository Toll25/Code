//Paul Hösch Array-Analyse 19.3.2021
package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        int j, i, temp, n, sum = 0;
        boolean swap;
        Scanner scan = new Scanner(System.in);

        System.out.print("Bitte geben sie die Anzahl ihrer Zahlen an: ");
        n = scan.nextInt();
        int[] numbers = new int[n];

        System.out.println("Bitte deine Zahlen eingeben: ");
        for (int l = 0; l < n; l++) {
            numbers[l] = scan.nextInt();
        }
        int min=numbers[1],max=numbers[1];

        for (int e : numbers){
            sum += e;
            if(e<min)
                min=e;
            if(e>max)
                max=e;
        }

        System.out.println("Das ist die Summe der Zahlen im Array: " + sum);

        sum = sum / numbers.length;
        System.out.println("Das ist der Durchschnitt der Zahlen im Array: " + sum);

        System.out.println("Das ist die größte Zahl im Array: " + max);

        System.out.println("Das ist die kleinste Zahl im Array: " + min);
    }
}