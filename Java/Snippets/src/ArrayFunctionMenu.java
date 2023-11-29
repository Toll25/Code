import java.io.File;

public class ArrayFunctionMenu {

    public static void main(String[] args) throws java.io.IOException {
        var scan = new java.util.Scanner(System.in);
        boolean on = true, nix = false;

        System.out.println("Menüpunkte:");
        System.out.println();
        System.out.println("1. Zahlen von Konsole lesen und in Array schreiben");
        System.out.println("2. Zahlen vom Array auf Konsole ausgeben");
        System.out.println("3. Zahlen im Array sortieren");
        System.out.println("4. Zahlen vom Array in ein  File schreiben");
        System.out.println("5. Zahlen von einem File einlesen und in Array speichern");
        System.out.println();
        System.out.println("0. Programm beenden");

        int n = 1;
        int[] arr = new int[n];
        do {
            System.out.println("Wähle einen Menüpunkt: ");
            int op = scan.next().charAt(0);
            switch (op) {
                case '1' -> {
                    System.out.println("Bitte geben sie die Anzahl ihrer Zahlen an: ");
                    n = scan.nextInt();
                    arr = new int[n];

                    System.out.println("Bitte deine Zahlen eingeben: ");
                    for (int l = 0; l < n; l++)
                        arr[l] = scan.nextInt();
                }
                case '2' -> {
                    for (int e : arr)
                        if (e != 0) {
                            System.out.println(e);
                        } else {
                            nix = true;
                        }
                    if (nix)
                        System.out.println("Keine Zahlen zum Anzeigen!");
                }
                case '3' -> {
                    boolean swap;
                    int j = arr.length, temp;
                    do {
                        j = j - 1;
                        swap = false;
                        for (int i = 0; i < j; i++) {
                            if (arr[i] > arr[i + 1]) {
                                temp = arr[i];
                                arr[i] = arr[i + 1];
                                arr[i + 1] = temp;
                                swap = true;
                            }
                        }
                    } while (swap);

                    for (int u : arr)
                        System.out.println(u);
                }
                case '4' -> {
                    var fileName = java.nio.file.Paths.get("zahlen.txt");
                    var writeZahlen = java.nio.file.Files.newBufferedWriter(fileName);

                    for (final int zahl : arr) {
                        writeZahlen.write(zahl + "\n");
                    }
                    writeZahlen.close();
                }
                case '5' -> {
                    var scan2 = new java.util.Scanner(new File("zahlen.txt"));
                    int i = 0;
                    while (scan2.hasNextInt()) {
                        arr[i++] = scan2.nextInt();
                    }
                    for (int u : arr)
                        System.out.println(u);
                    scan2.close();
                }
                case '0' -> on = false;
            }
        } while (on);
    }
}