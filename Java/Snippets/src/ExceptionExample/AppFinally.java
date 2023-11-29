package ExceptionExample;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class AppFinally {
    public AppFinally(){
        BufferedReader br= null;

        try {
            String line;
            br=new BufferedReader(new FileReader("text.txt"));
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch(FileNotFoundException ex){
            System.err.println("FileNotFoundException: " + ex.getMessage());
        } catch (IOException ex) {
            System.err.println("IOException: " + ex.getMessage());
        } finally {
            try {
                if (br != null) {
                    br.close();
                }
            } catch (IOException ex){
                System.err.println("IOException während br.close(): " + ex.getMessage());
            }
        }
    }

    public static void main(String[] args){

    }


}
