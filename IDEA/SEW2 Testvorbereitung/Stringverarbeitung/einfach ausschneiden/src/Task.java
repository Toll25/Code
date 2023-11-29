public class Task {
    // Aufgabenstellung:
    // von einem gegebenen Text soll ab dem Startindex die angegebene Länge herausgeschnitten werden
    // z.B. cut("Donaudampfschifffahrtskapitän", 5, 5) liefert "dampf"
    // Achtung: Wenn ab dem Startindex die angegebene Länge nicht mehr zur Verfügung steht, dann soll bis zum Ende des Textes ausgeschnitten werden
    // z.B. cut("Donaudampfschifffahrt", 16, 10)) liefert "fahrt"
    public String cut(String text, int startIndex, int laenge) {
        if ((startIndex+ laenge) > text.length()) {
            return text.substring(startIndex);
        }else{
            return text.substring(startIndex, startIndex+laenge);
        }
    }
}