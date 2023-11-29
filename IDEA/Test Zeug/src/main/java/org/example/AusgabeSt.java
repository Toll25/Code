package org.example;

public class AusgabeSt extends Ausgabe {
    public AusgabeSt(float betrag){
        this.betrag=betrag;
    }

    public float getSteuer(){
        return betrag*0.1667f;
    }
}
