public class EmailChecker {
    public static void main(String[] args) {
        String[] emails = {"john@doe.net", "john@doe.de", "rah@htlhl.at", "a@b.at", "jane@dee.shop", "jane@.net", "@.net", "a@.at"};
        for (String email : emails) {
            if (isEmail(email)) {
                System.out.println("Die Email >" + email + "< ist gültig. ");
            } else {
                System.out.println("Die Email >" + email + "< ist nicht gültig. ");
            }
        }
    }

    public static boolean isEmail(String email) {
        return (hasOneAtSign(email) && hasOneDot(email) && hasLocalPartNotEmpty(email) && hasHostNameNotEmpty(email) && hasValidTopLevelDomain(email));
    }

    private static boolean hasValidTopLevelDomain(String email) {
        return email.substring(email.indexOf('.') + 1).length() >= 2 && email.substring(email.indexOf('.') + 1).length() <= 3;
    }

    private static boolean hasHostNameNotEmpty(String email) {
        return !email.substring(email.indexOf('@') + 1, email.indexOf('.')).isEmpty();
    }

    private static boolean hasLocalPartNotEmpty(String email) {
        return !email.substring(0, email.indexOf('@')).isEmpty();
    }

    private static boolean hasOneDot(String email) {
        return email.indexOf('.') == email.lastIndexOf('.');
    }

    private static boolean hasOneAtSign(String email) {
        return email.indexOf('@') == email.lastIndexOf('@');
    }
}
