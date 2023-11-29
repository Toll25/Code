package com.company;

public class Song {
    private String title;
    private String interpreter;
    private int lengthInSeconds;

    public Song(String title, String interpreter, int lengthInSeconds) {
        this.title = title;
        this.interpreter = interpreter;
        this.lengthInSeconds = lengthInSeconds;
    }

    public String getlengthFormatted() {
        int minutes = lengthInSeconds / 60;
        int seconds = lengthInSeconds % 60;
        return (minutes + ":" + seconds);
    }

    @Override
    public String toString() {
        return (title + ", " + interpreter + ", " + lengthInSeconds + " sec.");
    }

    public boolean isEpic() {
        return lengthInSeconds >= 200;
    }

}