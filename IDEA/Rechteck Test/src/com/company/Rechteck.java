package com.company;

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
    // <a> x <b>;<color>;<isVisible>, z.B. 4 x 3;#7F7F7F;false
    @Override
    public String toString() {
        return a+" x "+b+";"+color+";"+isVisible;
    }

    // TODO 2: Erzeuge aus dem Eingabeformat (z.B. "4 x 3;#00FF00;true") ein Objekt Rechteck
    // Hinweis: boolean als String müssen wie float oder int umgewandelt werden z.B. Boolean.parseBoolean(<boolean var>)
    public static Rechteck valueOf(String text) {
        char delimiter = ';';
        int fstInd = text.indexOf(delimiter);
        int secInd = text.lastIndexOf(delimiter);
        String color = text.substring(fstInd + 1, secInd);
        String isVisible = text.substring(secInd + 1);
        String params = text.substring(0, fstInd);
        int xInd = params.indexOf('x');
        String aTemp = params.substring(0, xInd - 1);
        String bTemp = params.substring(xInd + 2);
        return new Rechteck(Integer.parseInt(aTemp), Integer.parseInt(bTemp), color, Boolean.parseBoolean(isVisible));
    }

    // TODO 3: Objekte von der Klasse Rechteck sind gleich,
    // 1. wenn die Attribute isVisible gleich sind,
    // 2. wenn die Attribute color gleich sind und
    // 3. wenn die Flächen gleich sind.
    @Override
    public boolean equals(Object other) {
        if (this == other) {
            return true;
        }
        if (!(other instanceof  Rechteck)){
            return false;
        }
        Rechteck o = (Rechteck) other;
        return (this.isVisible == o.isVisible) && (this.calculateArea() == o.calculateArea()) && (this.getColor().equals(o.getColor()));
    }

    // TODO 4: Beim Vergleich von Objekten der Klasse Rechteck soll
    // 1. das Attribut isVisible,
    // 2. die Farbe des Rechtecks und
    // 3. die Fläche des Rechtecks berücksichtigt werden.
    // Allgemeiner Hinweis für boolean Attribute:
    //  - wenn !this.<boolean_var> && other.<boolean_var>, dann -1,
    //  - wenn this.<boolean_var> && !other.<boolean_var>, dann 1,
    //  - sonst 0.

    /*
    * @author Paul Hösch
    * @param other
    * @return compare number
    */
    @Override
    public int compareTo(Rechteck other) {
        if (!this.isVisible && other.isVisible) {
            return -1;
        }else if (this.isVisible && !other.isVisible) {
            return 1;
        } else if (!(this.calculateArea() == other.calculateArea())) {
            return this.calculateArea()- other.calculateArea();
        } else {
            int diff = this.color.compareTo(other.color);
            return diff;
        }
    }

    public int getA() {
        return a;
    }

    public int getB() {
        return b;
    }

    public String getColor() {
        return color;
    }

    public boolean isVisible() {
        return isVisible;
    }
}
