public class Task {
    private static final char CURRENCY = '€';
    private static final char DELIMITER = ',';

    // Aufgabenstellung:
    // z.B. cutFirstCurrency("€100.12,€200.23,€300.99") liefert 100.12
    // Wenn keine Währung gefunden wird, dann soll 0.0 zurückgegeben werden
    // z.B. cutFirstCurrency("Hallo Welt") liefert 0.0
    public float cutFirstCurrency(String line) {
        int index= line.indexOf(CURRENCY);
        int index2 = line.indexOf(DELIMITER);
        if(index==-1){
            return (float) 0.0;
        }else{
            return Float.parseFloat(line.substring(index+1, index2 ));
        }
    }

    // Aufgabenstellung:
    // z.B. cutLastCurrency("€100.12,€200.23,€300.99") liefert 300.99
    // Wenn keine Währung gefunden wird, dann soll 0.0 zurückgegeben werden
    // z.B. cutLastCurrency("Hallo Welt") liefert 0.0
    public float cutLastCurrency(String line) {
        int index= line.lastIndexOf(CURRENCY);
        int index2= line.lastIndexOf(DELIMITER);
        if(index==-1){
            return (float) 0.0;
        }else{
            return Float.parseFloat(line.substring(index+1, index2));
        }
    }
}