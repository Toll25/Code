package com.company;

public class Main {
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
        return (hasOneAtSign() && hasOneDot() && hasLocalPartNotEmpty() && hasHostNameNotEmpty() && hasValidTopLevelDomain());
    }

    private static boolean hasValidTopLevelDomain() {
        return email.substring(email.indexOf('.') + 1).length() >= 2 && email.substring(email.indexOf('.') + 1).length() <= 3;
    }

    private static boolean hasHostNameNotEmpty() {
        return email.substring(email.indexOf('@') + 1, email.indexOf('.')).length() >= 1;
    }

    private static boolean hasLocalPartNotEmpty() {
        return email.substring(0, email.indexOf('@')).length() >= 1;
    }

    private static boolean hasOneDot() {
        return email.indexOf('.') == email.lastIndexOf('.');
    }

    private static boolean hasOneAtSign() {
        return email.indexOf('@') == email.lastIndexOf('@');
    }
}
}