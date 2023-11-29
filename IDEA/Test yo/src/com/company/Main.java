package com.company;

public class Main {

    public static void main(String[] args) throws java.io.IOException {
	final int NUMBER_OF_SONGS =100;

    Song[] songs = readSongs(NUMBER_OF_SONGS);

    var filePath =java.nio.file.Paths.get("NotEpicSongs.txt");
    var songWriter =java.nio.file.Files.newBufferedWriter(filePath);

    for (int i=0; i<songs.length;i++) {
        if (!songs[i].isEpic())
            songWriter.write(songs[i] + "\n");
    }
    songWriter.close();
    }

    private static Song[] readSongs(int numberOfSongs) {
        var scanner=new java.util.Scanner(System.in);
        Song[] songs =new Song[numberOfSongs];

        int countSongs=0;
        do{
            System.out.print("Titel des Songs: ");
            String title= scanner.nextLine();
            System.out.print("Interpret: ");;
            String interpreter =scanner.nextLine();
            System.out.print("Länge in Sekunden: ");
            int lengthInSeconds =scanner.nextInt();
            scanner.nextLine();

            Song i=new Song(title, interpreter, lengthInSeconds);
            songs[countSongs]=i;
            countSongs++;
        }while (countSongs < numberOfSongs);
        return songs;
    }
}
