// Starte zuerst mit der PhoneNumber.java Klasse!
public class Person {
    private String firstName;
    private char middleName;
    private String lastName;
    private PhoneNumber phoneNumber;

    public Person(String firstName, char middleName, String lastName, PhoneNumber phoneNumber) {
        this.firstName = firstName;
        this.middleName = middleName;
        this.lastName = lastName;
        this.phoneNumber = phoneNumber;
    }

    // Erzeuge aus dem Objekt einen String in folgendem Format:
    // z.B. "Franklin,D,Roosevelt,1/723/256" als Rückgabewert
    public String toString() {
        /* TODO 1 place your code here */;
    }

    // Erzeuge aus folgendem String-Format ein Person-Objekt
    // z.B. "Franklin,D,Roosevelt,1/723/256" als Übergabewert
    // Achte darauf, dass der vierte Wert (1/723/256) in ein PhoneNumber Objekt umgewandelt werden soll
    public static Person valueOf(String line) {
        /* TODO 2 place your code here */
    }

    public String getFirstName() {
        return firstName;
    }

    public char getMiddleName() {
        return middleName;
    }

    public String getLastName() {
        return lastName;
    }

    public PhoneNumber getPhoneNumber() {
        return phoneNumber;
    }
}