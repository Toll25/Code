
Spezielle Methoden, die eine Klasse beinhalten sollte:

## toString()

    @Override
    public String toString() {
       // eigene Implementierung
    }

Die toString()-Methode fasst die wichtigsten Informationen der Klasse zusammen und gibt sie in Form eines Strings zurück. Die String-Form ist die Darstellungsform für das menschliche Auge.

## equals()

    @Override     
    public boolean equals(Object other) {
       // 1. wenn die beiden Instanzen gleich sind

       // 2. wenn die Klassen nicht zusammenpassen

       // 3. ... und wenn die Attribute (Inhalte) gleich sind

       return ...;
    }

Bei Strings bzw. Objekten im Allgemeinen kann die inhaltliche Gleichheit **nicht** mit dem == Operator überprüft werden.
Mit dem == Operator werden die Referenzen (die Speicheradressen) überprüft.

Der == Operator darf nur für den Vergleich von elementaren Datentypen verwendet werden, d.h. bei char, boolean, int und float (und natürlich die restlichen Datentypen für Ganze Zahlen bzw. Dezimalzahlen).

Zum inhaltlichen Vergleich von zwei Objekten (*this*, die Instanz selbst mit *other*, einer ander Instanz der gleichen Klasse) muss daher ein anderer Weg gewählt werden.
Und zwar mit der equals()-Methode!

In der equals()-Methode muss genau festgelegt werden, welche Attribute verglichen werden müssen, um die inhaltliche Gleichheit zu bestätigen.

## compareTo()

    public class <T> implements Comparable<T> {

       @Override
       public int compareTo(<T> other) {

          rerturn ...;
       }
    }

In der compareTo()-Methode muss genau festgelegt werden, in welcher Reihenfolge die Attribute verglichen werden, um eine Reihung vornehmen zu können.

Zum Reihung von zwei Objekten (this, die Instanz selbst mit other, einer anderen Instanz der gleichen Klasse) wird das ganzzahlige Ergebnis wie folgt interpretiert:
* compareTo() liefert einen Wert kleiner als 0: this ist kleiner als other
* compareTo() liefert einen Wert gerößer als 0: this ist größer als other
* compareTo() liefert den Wert 0: this und other sind in der Reihenfolge gleich

## hashCode()

    @Override
    public int hashCode() {
        return Objects.hash(Attribut1, Attribut2, Attribut3, ...);
    }

Die Methode hashCode() liefert einen möglichst eindeutigen Wert in Form eines ints zur Identifikation des Inhalts eines Objektes zurück - ist also der equals-Methode ähnlich - erwartet aber keinen Übergabeparameter, da dieser Wert anhand der Eigenschaften des implementierenden Objekts berechnet wird.

Wenn zwei Objekte einen unterschiedlichen hashCode besitzen, können sie nicht inhaltlich gleich sein.
Besitzen zwei Objekte einen identischen hashCode, **können** sie inhaltlich gleich sein, **müssen aber nicht**. 

Die Methoden equals() und hashCode() sollten zusammen implementiert werden.
D.h. in die Berechnung von hashCodes dürfen nur Attribute einfliesen, die auch beim Vergleich mit equals berücksichtigt wurden.

## clone()

TBD