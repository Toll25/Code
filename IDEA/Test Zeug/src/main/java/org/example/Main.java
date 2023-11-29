package org.example;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        muster();
        ArrayList<AusgabeSt> ausgabeStArrayList= new ArrayList<>();
        Ausgabe.fill(ausgabeStArrayList);
        Ausgabe.print(ausgabeStArrayList);
    }


    public static void muster(){
        for(int i=0;i<5;i++){
            for(int j=0;j<i;j++)
                System.out.print("+");
            System.out.println("#####");
        }
    }

    public class F1Rennwagen{
        public void bremsen(){

        }
    }


}

