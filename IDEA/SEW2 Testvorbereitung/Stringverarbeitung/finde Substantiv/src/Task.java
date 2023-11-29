public class Task {
    // Aufgabenstellung:
    // Finde den ersten Namen, der mit dem übergebenen Startbuchstaben beginnt.
    // z.B. findFirstName("Anna; Beate; Clara; Ida; Jutta; Mona; Paula; Conny", 'B') liefert "Beate"
    //
    // Wenn Name nicht gefunden wird, dann Leerstring "" zurückgeben.
    // z.B. findFirstName("Anna; Beate; Clara; Ida; Jutta; Mona; Paula; Conny", 'Z') liefert ""
    public String findFirstName(String line, char startLetter) {
        int index = line.indexOf(startLetter);
        int index2 = line.indexOf(';', index);
    }
}