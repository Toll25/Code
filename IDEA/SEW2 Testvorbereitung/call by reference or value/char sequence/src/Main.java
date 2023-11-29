public class Main {

   // Aufgabenstellung:
   // Ergänze die System.out.println() mit den entsprechenden char-Werten
   public static void main(String[] args) {
      String justAString = "1First solution";
      char[] letters = justAString.toCharArray();
      // char-Wert für letters[0] bevor die Methode aufgerufen wurde
      System.out.println("1st letter=" + /* TODO 1 add char value for letters[0] */);
      boolean isSuccess = checkFirstLetter(letters);
      // char-Wert für letters[0], nachdem die Methode aufgerufen wurde
      System.out.println("1st letter=" + /* TODO 2 add char value for letters[0] */);
   }

   public static boolean checkFirstLetter(char[] letters) {
      letters[0] = '2';
      boolean hasFirstLetterChecked = true;
      return hasFirstLetterChecked;
   }
}