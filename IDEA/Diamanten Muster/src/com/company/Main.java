package com.company;

import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        // Create a new Scanner object
        Scanner scanner = new Scanner(System.in);

        // Get the number of rows from the user
        System.out.println("Geben Sie die Anzahl der Zeilen ein, die zum Drucken des Musters benötigt werden");

        int eingabe = scanner.nextInt();
        System.out.println("Diamant:");

        for (int druck=1; druck<=eingabe; druck++)
        {
            // Print space in decreasing order
            for (int leer=eingabe; leer>druck; leer--)
            {
                System.out.print(" ");
            }
            // Print star in increasing order
            for (int stern=1; stern<=(druck * 2) -1; stern++)
            {
                System.out.print("*");
            }
            System.out.println();
        }
        for (int druck=eingabe-1; druck>=1; druck--)
        {
            // Print space in increasing order
            for (int leer=eingabe-1; leer>=druck; leer--)
            {
                System.out.print(" ");
            }
            // Print star in decreasing order
            for (int stern=1; stern<=(druck * 2) -1; stern++)
            {
                System.out.print("*");
            }

            System.out.println();
        }
        scanner.close();
    }
}