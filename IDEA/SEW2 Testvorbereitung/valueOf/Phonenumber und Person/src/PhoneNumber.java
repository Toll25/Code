// Ergänze zuerst diese Klasse und wenn du diese fertig hast, dann mach bei der Person.java Klasse weiter
public class PhoneNumber {
    private int countryCode;
    private int areaCode;
    private int localPhoneNumber;

    public PhoneNumber(int countryCode, int areaCode, int localPhoneNumber) {
        this.countryCode = countryCode;
        this.areaCode = areaCode;
        this.localPhoneNumber = localPhoneNumber;
    }

    // Erzeuge aus dem Objekt einen String in folgendem Format:
    // z.B. "1/723/256" als Rückgabewert
    public String toString() {
        /* TODO 1 place your code here */
    }

    // Erzeuge aus folgendem String-Format ein PhoneNumber-Objekt
    // z.B. "1/723/256" als Übergabeparameter
    public static PhoneNumber valueOf(String line) {
        /* TODO 2 place your code here */
    }

    public int getCountryCode() {
        return countryCode;
    }

    public int getAreaCode() {
        return areaCode;
    }

    public int getLocalPhoneNumber() {
        return localPhoneNumber;
    }
}
