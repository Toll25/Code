package com.company;

public class Property {
    private String key;
    private String value;

    public Property(String key, String value) {
        this.key = key;
        this.value = value;
    }

    public String getKey() {
        return key;
    }

    public String getValue() {
        return value;
    }

    @Override
    public String toString() {
        return (key + "=" + value);
    }

    public boolean equals(Property platzhalter) {
        return (this.key.equals(platzhalter.key) && this.value.equals(platzhalter.value));
    }

    public static Property valueOf(String line) {
        int equals = line.indexOf('=');
        String key = line.substring(0, equals);
        String value = line.substring(equals + 1);
        return new Property(key, value);
    }
}
