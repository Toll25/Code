package org.example;

public class ConfigAccessSingleton {

    private static ConfigAccessSingleton instance;

    private ConfigAccessSingleton() {

    }

    public static synchronized ConfigAccessSingleton getInstance() {
        if(instance==null){
            instance=new ConfigAccessSingleton();
        }
        return instance;
    }

    public int readSettingOne(){
        return 42;
    }


    public void writeSettingOne(int settingOne){

    }

}
