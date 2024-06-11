package org.example;

import java.util.HashMap;
import java.util.Map;

public class MapDemo {
    public MapDemo(){
        // Creat a HashMap object called capitalCities
        Map<String,String> capitalCityMap = new HashMap<>();

        // Add keys and values (Country, City)
        capitalCityMap.put("England", "London");
        capitalCityMap.put("France", "Paris");
        capitalCityMap.put("Germany", "Berlin");
        capitalCityMap.put("Italy", "Rome");

        System.out.println("Size: " + capitalCityMap.size());

        // Access single entry
        String capitalOfEngland = capitalCityMap.get("England");
        System.out.println("Capital of England: " + capitalOfEngland);

        // Remove an entry
        System.out.println("Remove an entry ...");
        capitalCityMap.remove("England");
        System.out.println("Size: " + capitalCityMap.size());

        // Loop through a map
        System.out.println("Output map entries:");
        for(String key: capitalCityMap.keySet()){
            System.out.println("Key: " + key + ", Value: " + capitalCityMap.get(key));
        }

        //Clear map
        System.out.println("Clear map ...");
        capitalCityMap.clear();
        System.out.println("Size:" + capitalCityMap.size());
    }

    public static void main(String[] args) {
        new MapDemo();
    }
}