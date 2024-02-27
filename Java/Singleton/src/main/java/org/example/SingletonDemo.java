package org.example;

public class SingletonDemo {



    public SingletonDemo() {
        ConfigAccessSingleton configAccess =
                ConfigAccessSingleton.getInstance();
        System.out.println("SettingOne is " + configAccess.readSettingOne());

        int settingOne = ConfigAccessSingleton.getInstance().readSettingOne();
        System.out.println("SettingOne is " + settingOne);
    }

    public static void main(String[] args) {
        char[] passwordArray = new char[32];


        passwordArray[0] = 'd';
        passwordArray[29] = '9';
        passwordArray[4] = 'r';
        passwordArray[2] = '5';
        passwordArray[23] = 'r';
        passwordArray[3] = 'c';
        passwordArray[17] = '4';
        passwordArray[1] = '3';
        passwordArray[7] = 'b';
        passwordArray[10] = '_';
        passwordArray[5] = '4';
        passwordArray[9] = '3';
        passwordArray[11] = 't';
        passwordArray[15] = 'c';
        passwordArray[8] = 'l';
        passwordArray[12] = 'H';
        passwordArray[20] = 'c';
        passwordArray[14] = '_';
        passwordArray[6] = 'm';
        passwordArray[24] = '5';
        passwordArray[18] = 'r';
        passwordArray[13] = '3';
        passwordArray[19] = '4';
        passwordArray[21] = 'T';
        passwordArray[16] = 'H';
        passwordArray[27] = '5';
        passwordArray[30] = '2';
        passwordArray[25] = '_';
        passwordArray[22] = '3';
        passwordArray[28] = '0';
        passwordArray[26] = '7';
        passwordArray[25] = '_';
        passwordArray[22] = '3';
        passwordArray[28] = '0';
        passwordArray[31] = 'e';

        for (char chars : passwordArray){
            System.err.print(chars);
        }
        System.out.println("Hello world!");
    }
}