package org.example;

public class MySingleton {
    public static MySingleton instance = new MySingleton();
    public String value;

    private MySingleton() {
        value = "my name :)";
    }

    public static synchronized MySingleton getInstance(){
        if (instance == null) {
            instance = new MySingleton();
        }
        return instance;
    }

    public String getValue(){
        return value;
    }


    
}
