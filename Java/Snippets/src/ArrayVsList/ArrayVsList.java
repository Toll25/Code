package ArrayVsList;

import java.util.ArrayList;

/**
 * Dieses beispiel zeigt die Unterschiede zwischen einem array und einer Liste.
 *
 * Das Arbeiten mit Listen bietet dem Programmierer viele Erleichterungen
 * gegenüber dem Arbeiten direkt mit Arrays
 *
 * z.B.:
 *  o einfaches Hinzufügen und Entfernen von Datensätzen
 *  o einfacher Zugriff auf Elemente (nicht nur über Index)
 *  o u.v.m.
 *
 * @author Paul Hösch
 * @version 2022-09-14
 */

public class ArrayVsList {

    // Fields +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    String[] myArray;
    private ArrayList<String> myList;

    // Instance creation ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    public ArrayVsList(){
        myArray=new String[4];
        myList=new ArrayList<String>();
        fill();
        showContents();
        removeValue("ist");
        showContents();
    }

    // Private Methods ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    private void fill() {
        //Fill array with values
        myArray[0] = "Heute";
        myArray[1] = "ist";
        myArray[2] = "es";
        myArray[3] = "schön";

        //Fill list with values
        myList.add("Heute");
        myList.add("ist");
        myList.add("es");
        myList.add("schön");
    }

    private void showContents(){
        System.out.println("Show array content:");
        for(String c:myArray){
            System.out.print(c);
            System.out.print(" ");
        }

        System.out.println();

        System.out.println("Show list content:");
        for(String value:myList){
            System.out.print(value);
            System.out.print(" ");
        }
    }

    private void removeValue(String value){
        /*System.out.println("Trying to remove value'"+value+"'");
        // Set found array entry to null
        for(int i=0; i< myArray.length; i++)
            if(myArray[i]!=null && myArray[i].equals(value))
                myArray[i]=null;
        //Remove found entry in list
        int detectedIndex=-1;
        for(int i=0; i< myList.size();i++){
            if(myList.get(i).equals(value)){
                detectedIndex=i;
            }
        }

        if(detectedIndex >= 0){
            myList.remove(detectedIndex);
        }

         */

        System.out.println("Length of list before removal: " + myList.size());
        myList.remove(value);

        System.out.println("Length of list after removal: " + myList.size());

    }

    // Main +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    public static void main(String[] args) {
        new ArrayVsList();

    }
}