package com.company;

// Comments:
// ...

// TODO: Ergänze dein Package

public class Main {
    public static void main(String[] args) {
        /*
        String[] lines = {"Vorname=Max", "Nachname=Mustermann", "Geburtsdatum=19990131", "Wohnort=Hollabrunn",
                "Postleitzahl=2020"};
        /*
        // Diese Arrays sollen mittels Stringverarbeitung befüllt werden
        // Das Array keys soll alle Schlüsselwörter (=keys) vor dem '=' beinhalten
        String[] keys = new String[lines.length];
        // Das Array values soll alle Werte (=values) nach dem '=' beinhalten
        String[] values = new String[lines.length];

        // TODO: Die einzelnen "lines" sollen hier in Schlüsselwörter und Werte getrennt werden und
        //       in die Arrays keys und values geschrieben werden.
        //       Die nachfolgenden Tests zeigen dir, ob dein Code richtig ist!
        //  Place your code here ...
*/
        /*
        Property[] properties = new Property[lines.length];

        for (int i = 0; i < lines.length; i++) {
            properties[i] = Property.valueOf(lines[i]);
        }


        // Test: Don't change!
        {
            // Diese Arrays sind nur für Testzwecke
            String[] expectedKeys = {"Vorname", "Nachname", "Geburtsdatum", "Wohnort", "Postleitzahl"};
            String[] expectedValues = {"Max", "Mustermann", "19990131", "Hollabrunn", "2020"};
            for (int i = 0; i < lines.length; i++) {
                System.out.println("given: " + lines[i]);
                System.out.println("expected key: " + expectedKeys[i] + ", expected value: " + expectedValues[i]);
                System.out.println("  result key: " + properties[i].getKey() + ",   result value: " + properties[i].getValue());
                System.out.println("is key equal: " + expectedKeys[i].equals(properties[i].getKey()) + ", is value equal: " + expectedValues[i].equals(properties[i].getValue()));
                System.out.println();
            }
        }


        String[] namen = {"Daisy", "Luigi", "Mario", "Bowser", "Waluigi"};

        System.out.println("unsorted: " + Arrays.toString(namen));
        Arrays.sort(namen);
        System.out.println("sorted: " + Arrays.toString(namen));

        Date date1 = new Date (2022, 3, 8);
        Date date2 = new Date (2023, 5, 9);
        Date date3 = new Date (2018, 10, 9);
        Date date4 = new Date (2025, 5, 5);
        System.out.println(date1.compareTo(date2));

        Date[] daten={ date1, date2, date3, date4};
        System.out.println(Arrays.toString(daten));
        Arrays.sort(daten);
        System.out.println(Arrays.toString(daten));

        /*
        for(int i=0; i<namen.length-1; i++) {
                System.out.println("Compared " + namen[i] + " with " + namen[i+1]);
                System.out.println(namen[i].compareTo(namen[i + 1]));
        }



        int[] nums = {1, 2, 3, 4};

        int total = sumOfDouble(nums);

        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + ", ");
        }
        System.out.println("The Sum of these numbers is " + total);
    }

    private static int sumOfDouble(int[] numbers) {
        int [] numbersDup = new int [numbers.length];

        System.arraycopy(numbers, 0, numbersDup, 0, numbers.length);

        int total = 0;
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = numbers[i] * 2;
            total += numbers[i];
        }
        return total;*/


    }
}