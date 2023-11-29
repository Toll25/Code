public class Rechteck implements Comparable<Rechteck> {
    private int a;
    private int b;
    private String color; // RGB Farbwert in Hex-Darstellung: z.B schwarz = #000000, grau = #7F7F7F oder gelb = #FFFF00
    // bessere Datentyp wäre int mit der Hexadezimaldarstellung z.B. 0x7F7F7F
    private boolean isVisible;

    public Rechteck(int a, int b, String color, boolean isVisible) {
        this.a = a;
        this.b = b;
        this.color = color.toUpperCase();
        this.isVisible = isVisible;
    }

    public int calculateArea() {
        return a * b;
    }

    // TODO 1: Ergänze die toString()-Methode für das folgende Ausgabeformat.
    // Format: <a> x <b>;<color>;<isVisible>, z.B. 4 x 3;#7F7F7F;false
    @Override
    public String toString() {

        /* TODO 1 ergänze die toString()-Methode */
    }

    // TODO 2: Erzeuge aus dem Eingabeformat (z.B. "4 x 3;#00FF00;true") ein Objekt Rechteck
    // Hinweis: boolean als String müssen wie float oder int umgewandelt werden z.B. Boolean.parseBoolean(<boolean var>)
    public static Rechteck valueOf(String text) {
        /* TODO 2 Ergänze die valueOf()-Methode */
    }

    // TODO 3: Objekte von der Klasse Rechteck sind gleich,
    // 1. wenn die Attribute isVisible gleich sind,
    // 2. wenn die Attribute color gleich sind und
    // 3. wenn die Flächen gleich sind.
    @Override
    public boolean equals(Object other) {
        /* TODO 3 Ergänze die equals()-Methode */
    }

    // TODO 4: Beim Vergleich von Objekten der Klasse Rechteck soll
    // 1. das Attribut isVisible,
    // 2. die Farbe des Rechtecks und
    // 3. die Fläche des Rechtecks berücksichtigt werden.
    // Allgemeiner Hinweis für boolean Attribute:
    //  - wenn !this.<boolean_var> && other.<boolean_var>, dann -1,
    //  - wenn this.<boolean_var> && !other.<boolean_var>, dann 1,
    //  - sonst 0.
    @Override
    public int compareTo(Rechteck other) {
        /* TODO 4 Ergänze die compareTo()-Methode */
    }
}