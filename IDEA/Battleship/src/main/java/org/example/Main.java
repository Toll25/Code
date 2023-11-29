package org.example;
import java.util.Objects;
import java.util.Scanner;

public class Main {

    enum BoatType {
        Carrier,
        Battleship1,
        Battleship2,
        Cruiser1,
        Cruiser2,
        Cruiser3,
        Submarine1,
        Submarine2,
        Submarine3,
        Destroyer1,
        Destroyer2,
        Destroyer3,
        Destroyer4
    }

    public static void onSink(Field[][] a, Main.BoatType t) {
        for (Field[] b : a)
            for (Field c : b) {
                if (c.partOfBoat == t) {
                    c.display = "*";
                }
            }
    }

    public static void show10(Field[][] playingField, int shots) {
        System.out.println("  | A | B | C | D | E | F | G | H | I | J |");
        System.out.println("--+---+---+---+---+---+---+---+---+---+---+");
        int i = 1;
        for (Field[] row : playingField) {
            System.out.print(i);
            if (i < 10)
                System.out.print(" ");
            i++;
            System.out.print("| ");
            for (Field x : row) {
                System.out.print(x.display + " | ");
            }
            System.out.println();
            System.out.println("--+---+---+---+---+---+---+---+---+---+---+");
        }
        System.out.println("Shots left: " + shots);
    }

    public static void show8(Field[][] playingField, int shots) {
        System.out.println("  | A | B | C | D | E | F | G | H |");
        System.out.println("--+---+---+---+---+---+---+---+---+");
        int i = 1;
        for (Field[] row : playingField) {
            System.out.print(i);
            System.out.print(" ");
            i++;
            System.out.print("| ");
            for (Field x : row) {
                System.out.print(x.display + " | ");
            }
            System.out.println();
            System.out.println("--+---+---+---+---+---+---+---+---+");
        }
        System.out.println("Shots left: " + shots);
    }

    public static void show6(Field[][] playingField, int shots) {
        System.out.println("  | A | B | C | D | E | F |");
        System.out.println("--+---+---+---+---+---+---+");
        int i = 1;
        for (Field[] row : playingField) {
            System.out.print(i);
            System.out.print(" ");
            i++;
            System.out.print("| ");
            for (Field x : row) {
                System.out.print(x.display + " | ");
            }
            System.out.println();
            System.out.println("--+---+---+---+---+---+---+");
        }
        System.out.println("Shots left: " + shots);
    }

    public static Field[][] setup(int num) {
        Field[][] playingField = new Field[num][num];
        for (int i = 0; i <= num - 1; i++)
            for (int j = 0; j <= num - 1; j++) {
                playingField[i][j] = new Field(false);
            }
        return playingField;
    }

    public static void main(String[] args) throws InterruptedException {
        Scanner scan = new Scanner(System.in);
        System.out.println(" -Unknown");
        System.out.println("O-Empty");
        System.out.println("X-Hit");
        System.out.println("*-Sunk");
        System.out.println();
        System.out.println("Start? (Y/N):");
        String start = scan.nextLine();

        if (Objects.equals(start, "Y") || Objects.equals(start, "y")) {

            System.out.println("Wich size? (10, 8, 6)");
            String size = scan.nextLine();

            if (Objects.equals(size, "10") || Objects.equals(size, "8") || Objects.equals(size, "6")) {


                Field[][] playingField = new Field[0][0];

                int limit = 0;
                int shots = 0;
                int winCond = 0;
                String letterLimit = "a";

                switch (size) {
                    case "10" -> {
                        limit = 10;
                        playingField = setup(10);
                        shots = 25;
                        winCond = 13;
                        letterLimit = "j";
                    }
                    case "8" -> {
                        limit = 8;
                        playingField = setup(8);
                        shots = 20;
                        winCond = 10;
                        letterLimit = "h";
                    }
                    case "6" -> {
                        limit = 6;
                        playingField = setup(6);
                        shots = 15;
                        winCond = 7;
                        letterLimit = "f";
                    }
                }

                int Car = 0;
                int Bat1 = 0;
                int Bat2 = 0;
                int Cru1 = 0;
                int Cru2 = 0;
                int Cru3 = 0;
                int Sub1 = 0;
                int Sub2 = 0;
                int Sub3 = 0;
                int Des1 = 0;
                int Des2 = 0;
                int Des3 = 0;
                int Des4 = 0;

                int shipsSunk = 0;

                boolean vertvalid = false;
                boolean horivalid = false;

                RandomShip.shipPlacer(playingField, BoatType.Destroyer1, RandomShip.makeRandomXPointModus(Integer.parseInt(size)), RandomShip.makeRandomYPointModus(Integer.parseInt(size)), true);

                for(Field[] i: playingField)
                    for(Field j:i)
                        if(!(j.partOfBoat==null))
                            Field.onHit(j);

                do {
                    switch (size) {
                        case "10" -> show10(playingField, shots);
                        case "8" -> show8(playingField, shots);
                        case "6" -> show6(playingField, shots);
                    }

                    System.out.println("Coordinates (e.g.: a2): ");
                    String coord = scan.nextLine();

                    String vert = coord.substring(1);
                    int cord1 = (Integer.parseInt(vert) - 1);
                    if (cord1 >= 0 && cord1 < limit)
                        vertvalid = true;


                    int cord2 = 0;
                    String hori = coord.substring(0, 1);
                    hori = hori.toLowerCase();
                    if (hori.compareTo(letterLimit) > 0) {
                        horivalid = false;
                    } else {
                        final String alphabet = "abcdefghijklmnopqrstuvwxyz";
                        cord2 = alphabet.indexOf(hori.charAt(0));
                        if (cord2 >= 0 && cord2 <= limit)
                            horivalid = true;
                    }

                    boolean didHit = false;
                    BoatType whatHit = null;

                    if (vertvalid && horivalid) {

                        if (playingField[cord1][cord2].hit) {
                            System.out.println("Already hit!");
                            shots++;
                        } else if (!((playingField[cord1][cord2].partOfBoat) == null)) {
                            System.out.println("Hit!");
                            Field.onHit(playingField[cord1][cord2]);
                            didHit = true;
                            whatHit = playingField[cord1][cord2].partOfBoat;
                        } else {
                            System.out.println("Miss!");
                            Field.onMiss(playingField[cord1][cord2]);
                        }


                        if (didHit) {
                            switch (whatHit) {
                                case Carrier -> {
                                    Car++;
                                    if (Car == 5) {
                                        System.out.println("Carrier Sunk!");
                                        shipsSunk++;
                                        Car++;
                                        onSink(playingField, BoatType.Carrier);
                                    }
                                }
                                case Battleship1 -> {
                                    Bat1++;
                                    if (Bat1 == 4) {
                                        System.out.println("Battleship 1 Sunk!");
                                        shipsSunk++;
                                        Bat1++;
                                        onSink(playingField, BoatType.Battleship1);
                                    }
                                }
                                case Battleship2 -> {
                                    Bat2++;
                                    if (Bat2 == 4) {
                                        System.out.println("Battleship 2 Sunk!");
                                        shipsSunk++;
                                        Bat2++;
                                        onSink(playingField, BoatType.Battleship2);
                                    }
                                }
                                case Cruiser1 -> {
                                    Cru1++;
                                    if (Cru1 == 3) {
                                        System.out.println("Cruiser 1 Sunk!");
                                        shipsSunk++;
                                        Cru1++;
                                        onSink(playingField, BoatType.Cruiser1);
                                    }
                                }
                                case Cruiser2 -> {
                                    Cru2++;
                                    if (Cru2 == 3) {
                                        System.out.println("Cruiser 2 Sunk!");
                                        shipsSunk++;
                                        Cru2++;
                                        onSink(playingField, BoatType.Cruiser2);
                                    }
                                }
                                case Cruiser3 -> {
                                    Cru3++;
                                    if (Cru3 == 3) {
                                        System.out.println("Cruiser 3 Sunk!");
                                        shipsSunk++;
                                        Cru3++;
                                        onSink(playingField, BoatType.Cruiser3);
                                    }
                                }
                                case Submarine1 -> {
                                    Sub1++;
                                    if (Sub1 == 3) {
                                        System.out.println("Submarine 1 Sunk!");
                                        shipsSunk++;
                                        Sub1++;
                                        onSink(playingField, BoatType.Submarine1);
                                    }
                                }
                                case Submarine2 -> {
                                    Sub2++;
                                    if (Sub2 == 3) {
                                        System.out.println("Submarine 2 Sunk!");
                                        shipsSunk++;
                                        Sub2++;
                                        onSink(playingField, BoatType.Submarine2);
                                    }
                                }
                                case Submarine3 -> {
                                    Sub3++;
                                    if (Sub3 == 3) {
                                        System.out.println("Submarine 3 Sunk!");
                                        shipsSunk++;
                                        Sub3++;
                                        onSink(playingField, BoatType.Submarine3);
                                    }
                                }
                                case Destroyer1 -> {
                                    Des1++;
                                    if (Des1 == 2) {
                                        System.out.println("Destroyer 1 Sunk!");
                                        shipsSunk++;
                                        Des1++;
                                        onSink(playingField, BoatType.Destroyer1);
                                    }
                                }
                                case Destroyer2 -> {
                                    Des2++;
                                    if (Des2 == 2) {
                                        System.out.println("Destroyer 2 Sunk!");
                                        shipsSunk++;
                                        Des2++;
                                        onSink(playingField, BoatType.Destroyer2);
                                    }
                                }
                                case Destroyer3 -> {
                                    Des3++;
                                    if (Des3 == 2) {
                                        System.out.println("Destroyer 3 Sunk!");
                                        shipsSunk++;
                                        Des3++;
                                        onSink(playingField, BoatType.Destroyer3);
                                    }
                                }
                                case Destroyer4 -> {
                                    Des4++;
                                    if (Des4 == 2) {
                                        System.out.println("Destroyer 4 Sunk!");
                                        shipsSunk++;
                                        Des4++;
                                        onSink(playingField, BoatType.Destroyer4);
                                    }
                                }
                            }

                        }

                        if (shipsSunk == winCond) {
                            System.out.println("You Win!!");
                        }
                        shots--;
                    } else {
                        System.out.println("Invalid Input");
                    }
                    Thread.sleep(1000);
                } while (shots > 0);
            } else {
                System.out.println("Invalid Size");
            }
        }
    }
}