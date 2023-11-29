public class Task {
    // TODO: Finde das letzte Wort, das mit dem übergebenen String beginnt.
    // z.B. findLastWord("Beachte,Analog,Beamte,Diagramm,Beate,Heraus,Besen", "Be") liefert "Besen"
    //
    // Wenn das Wort nicht gefunden wird, dann Leerstring "" zurückgeben.
    // z.B. findLastWord("Beachte,Analog,Beamte,Diagramm,Beate,Heraus,Besen", "Ge") liefert ""
    public String findLastWord(String line, String startString) {
        char delimiter = ',';
        int lastIndex = line.lastIndexOf(startString);
        if (lastIndex == -1) {
            return "";
        }
        return line.substring(lastIndex);
    }
}