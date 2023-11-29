package com.company;

public class Book {
    private final String title;
    private final String isbn;
    private final int pagescount;
    private Date publishingDate;

    public Book(String title, String isbn, int pagescount) {
        this.title = title;
        this.isbn = isbn;
        this.pagescount = pagescount;
        this.publishingDate=new Date(2021, 8, 12);
    }

    public Book(String title, String isbn, int pagescount, Date publishingDate) {
        this.title = title;
        this.isbn = isbn;
        this.pagescount = pagescount;
        this.publishingDate=publishingDate;
    }

    public Date getPublishingDate() {
        return publishingDate;
    }

    public boolean isGermanLanguage() {
        return isbn.charAt(4) == '3';
    }

    @Override
    public String toString() {
        return "Book[" + title + ", " + isbn + ", " + pagescount + "]";
    }

    public boolean isNovel() {
        return pagescount >= 101 && pagescount <= 250;
    }

    public static Book valueOf(String string) {
        int firstSeperator = string.indexOf(',');
        int lastSeperator = string.lastIndexOf(',');

        String title = string.substring(0, firstSeperator);
        String isbn = string.substring(firstSeperator + 1, lastSeperator);
        String pagesCountString = string.substring(lastSeperator + 1);

        int pagesCount = Integer.parseInt(pagesCountString);
        return new Book(title, isbn, pagesCount);
    }
    public void setPublishingDate(Date publishingDate){
        this.publishingDate=publishingDate;
    }

    public String getFormatted(){
        return title+"; "+isbn+"; " +pagescount;
    }
}