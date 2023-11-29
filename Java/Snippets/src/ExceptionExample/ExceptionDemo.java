package ExceptionExample;

import java.util.ArrayList;

public class ExceptionDemo {

    public ExceptionDemo(){
        demo1();
    }

    private void demo1(){
        try{
            int wert=Integer.valueOf("Keine Zahl");
            //int wert=Integer.valueOf("11");
            ArrayList<String> nameList=null;
            //nameList.add("Tim");
        } catch (NumberFormatException ex){
            System.err.println("Can´t parse Integer" + ex.getMessage());
        } catch (NullPointerException ex) {
            System.err.println("Nullpointerexception aufgetreten");
        }
    }

    public static void main(String[] args) {
        ExceptionDemo gaming=new ExceptionDemo();
    }
}