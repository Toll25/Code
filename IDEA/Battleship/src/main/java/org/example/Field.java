package org.example;

public class Field {
    String display;
    boolean hit;
    Main.BoatType partOfBoat;

    public Field(boolean hit){
        this.display=" ";
        this.hit=hit;
        this.partOfBoat=null;
    }

    public void setPartOfBoat(Main.BoatType value){
        partOfBoat=value;
    }

    public Main.BoatType getPartOfBoat(){
        return partOfBoat;
    }

    public static void onHit(Field c) {
        c.display="X";
        c.hit=true;
    }

    public static void onMiss(Field c) {
        c.display="O";
        c.hit=true;
    }

}
