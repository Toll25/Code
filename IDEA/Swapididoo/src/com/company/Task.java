package com.company;

public class Task {
    private static final char CURRENCY = '€';
    private static final char DELIMITER = ',';

    // Aufgabenstellung:
    // z.B. cutFirstCurrency("€100.12,€200.23,€300.99") liefert 100.12
    // Wenn keine Währung gefunden wird, dann soll 0.0 zurückgegeben werden
    // z.B. cutFirstCurrency("Hallo Welt") liefert 0.0
    public static float cutFirstCurrency(String line) {
        if(line.indexOf(CURRENCY) == -1){
            return (float) 0;
        }else{
            return Float.parseFloat(line.substring(line.indexOf(CURRENCY)+1, line.indexOf(DELIMITER)));
        }}

    // Aufgabenstellung:
    // z.B. cutLastCurrency("€100.12,€200.23,€300.99") liefert 300.99
    // Wenn keine Währung gefunden wird, dann soll 0.0 zurückgegeben werden
    // z.B. cutLastCurrency("Hallo Welt") liefert 0.0
    public static float cutLastCurrency(String line) {
        if(line.indexOf(CURRENCY) == -1){
            return (float) 0;
        }else{
            return Float.parseFloat(line.substring(line.lastIndexOf(CURRENCY)+1));
        }
    }
}