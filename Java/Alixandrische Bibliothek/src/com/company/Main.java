package com.company;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {

    public static void main(String[] args) throws java.io.IOException {
        final int NUMBER_OF_BOOKS = 1;
        readBooksFile();
        Book[] allBooks = readBooks(NUMBER_OF_BOOKS);

        var filePath = java.nio.file.Paths.get("NotNovels.txt");
        var bookWriter = java.nio.file.Files.newBufferedWriter(filePath);

        var csvPath = java.nio.file.Paths.get("books.csv");
        var csvWriter = java.nio.file.Files.newBufferedWriter(csvPath);
        // TODO 9: Gehe Buch für Buch durch. Wenn das Buch KEINE Novelle ist
        // (rufe dazu die Methode isNovel() auf), dann schreibe das Buch in eine neue Zeile im File.
        for (int i = 0; i < NUMBER_OF_BOOKS; i++) {
            csvWriter.write(allBooks[i].getFormatted() + "\n");
            if (!allBooks[i].isNovel()) {
                bookWriter.write(allBooks[i].toString() + allBooks[i].getPublishingDate().toString() + "\n");
            }
        }
        bookWriter.close();
        csvWriter.close();
    }
    public static Book[] readBooksFile() throws IOException {
        var filePaths = Paths.get("books.csv");
        for (String line: Files.readAllLines(filePaths)){
            System.out.println(line);
        }
        return null;
    }

    private static Book[] readBooks(int numberOfBooks) {
        var scanner = new java.util.Scanner(System.in);
        // TODO 6: Deklariere und initialisiere ein Book-Array mit dem Namen myBooks.
        Book[] myBooks = new Book[numberOfBooks];

        int booksCount = 0;
        do {
            /*System.out.print("Titel des Buches: ");
            String title = scanner.nextLine();
            System.out.print("ISBN: ");
            String isbn = scanner.nextLine();
            System.out.print("Anzahl der Buchseiten: ");
            int pagesCount = scanner.nextInt();
            scanner.nextLine();
            Date defaulDate=new Date(2022, 1, 1);
            // TODO 7: Erzeuge ein Buch Objekt mit dem Variablennamen oneBook
            Book oneBook = new Book(title, isbn, pagesCount, defaulDate);*/
            System.out.println("Titel des Buches, ISBN, Anzahl der Buchseiten");
            String scan = scanner.nextLine();
            Book oneBook = Book.valueOf(scan);

            System.out.println(oneBook + ", deutschsprachig: " + oneBook.isGermanLanguage());
            // TODO 8: Nimm das Book Objekt im Array auf. Inkrementiere auch den Book Counter.
            myBooks[booksCount++] = oneBook;

        } while (booksCount < numberOfBooks);
        return myBooks;
    }
}