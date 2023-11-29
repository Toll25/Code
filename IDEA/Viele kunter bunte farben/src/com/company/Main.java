package com.company;

import java.util.Random;

public class Main {

    enum color {
        Black,
        Red,
        Green,
        Blue,
        Yellow,
        White,
        Orange,
        Magenta;

        @Override
        public String toString() {
            return switch (this) {
                case Black -> "Schwarz";

                case Red -> "Rot";

                case Green -> "Grün";

                case Blue -> "Blau";

                case Yellow -> "Gelb";

                case White -> "Weiß";

                case Orange -> "Orange";

                case Magenta -> "Magenta";

            };
        }
    }

    public static StringBuilder printAvailableColors() {
        color[] colors = color.values();
        StringBuilder out = new StringBuilder("| ");
        int point = 0;
        for (color color : colors) {
            out.append(point + "=" + color.toString() + " | ");
            point++;
        }
        return out;
    }

    public static color fromOrdinal(final int ordinal) {
        return color.values()[ordinal];
    }

    public static color generateRandomColor() {
        Random rand = new Random();
        int upperbound = color.values().length;
        int int_random = rand.nextInt(upperbound);
        return fromOrdinal(int_random);
    }


    public static void main(String[] args) {


        System.out.println(generateRandomColor());
        System.out.println(generateRandomColor());

// Print all available colors
        System.out.println(printAvailableColors());

// Get Color from ordinal
        System.out.println(fromOrdinal(3).toString());

    }
}
