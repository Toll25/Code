public class Task {
    // Aufgabenstellung:
    // von einem gegebenen Text soll von vorne die angegebene Länge weggeschnitten werden
    // z.B. cutStart("Donaudampfschifffahrt", 5) liefert "dampfschifffahrt"
    // Achtung: Wenn beim Wegschneiden von vorne nichts mehr übrig bleibt, dann soll ein Leerstring zurückgegeben werden
    // z.B. z.B. cutStart("Hallo", 10) liefert ""
    public String cutStart(String text, int cutSize) {
        if(cutSize>text.length()){
            return "";
        }else{
            return text.substring(cutSize);
        }
    }

    // Aufgabenstellung:
    // von einem gegebenen Text soll von hinten die angegebene Länge weggeschnitten werden
    // z.B. cutEnd("Donaudampfschifffahrt", 5) liefert "Donaudampfschiff"
    // Achtung: Wenn beim Wegschneiden von hinten nichts mehr übrig bleibt, dann soll ein Leerstring zurückgegeben werden
    // z.B. z.B. cutEnd("Hallo", 10) liefert ""
    public String cutEnd(String text, int cutSize) {
        if ( cutSize>text.length()){
            return "";
        }else{
            return text.substring(0, text.length()-cutSize);
        }
    }
}