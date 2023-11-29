package org.example;

import java.awt.*;
import java.awt.geom.Point2D;
import java.util.Random;


public class RandomShip {


    private static int coordinatesRandomX = 0;
    private static int coordinatesRandomY = 0;

    Point2D p = new Point();

    // Kollisionsfreiheit
    // Mit einer Schleife aber neu zufalls
    // Horizontal und Vertical


    public static int makeRandomXPointModus(int size) {
        int min = 0;
        int max = size - 2;
        return coordinatesRandomX = (int) Math.floor(Math.random() * (max - min + 1) + min);
    }

    public static int makeRandomYPointModus(int size) {
        int min = 0;
        int max = size - 2;
        return coordinatesRandomY = (int) Math.floor(Math.random() * (max - min + 1) + min);
    }

    public static void shipPlacer(Field[][] playingField, Main.BoatType kindOfShip, int cord1, int cord2, boolean orientation) {
        if (orientation) {
            playingField[cord1][cord2].setPartOfBoat(kindOfShip);
            playingField[cord1][cord2 + 1].setPartOfBoat(kindOfShip);
            switch (kindOfShip) {
                case Carrier -> {
                    playingField[cord1][cord2 + 2].setPartOfBoat(kindOfShip);
                    playingField[cord1][cord2 + 3].setPartOfBoat(kindOfShip);
                    playingField[cord1][cord2 + 4].setPartOfBoat(kindOfShip);
                }
                case Battleship1, Battleship2 -> {
                    playingField[cord1][cord2 + 2].setPartOfBoat(kindOfShip);
                    playingField[cord1][cord2 + 3].setPartOfBoat(kindOfShip);
                }
                case Cruiser1, Cruiser2, Cruiser3, Submarine1, Submarine2, Submarine3 ->
                        playingField[cord1][cord2 + 2].setPartOfBoat(kindOfShip);
            }
        } else {
            playingField[cord1][cord2].setPartOfBoat(kindOfShip);
            playingField[cord1 + 1][cord2].setPartOfBoat(kindOfShip);
            switch (kindOfShip) {
                case Carrier -> {
                    playingField[cord1 + 2][cord2].setPartOfBoat(kindOfShip);
                    playingField[cord1 + 3][cord2].setPartOfBoat(kindOfShip);
                    playingField[cord1 + 4][cord2].setPartOfBoat(kindOfShip);
                }
                case Battleship1, Battleship2 -> {
                    playingField[cord1 + 2][cord2].setPartOfBoat(kindOfShip);
                    playingField[cord1 + 3][cord2].setPartOfBoat(kindOfShip);
                }
                case Cruiser1, Cruiser2, Cruiser3, Submarine1, Submarine2, Submarine3 ->
                        playingField[cord1 + 2][cord2].setPartOfBoat(kindOfShip);
            }
        }
    }


}