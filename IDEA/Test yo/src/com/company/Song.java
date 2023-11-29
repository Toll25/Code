package com.company;

public class Song {
    private String title;
    private String interpreter;
    private int lengthInSeconds;

    public Song (String title, String interpreter, int lengthInSeconds) {
        this.title = title;
        this.interpreter = interpreter;
        this.lengthInSeconds = lengthInSeconds;
    }

    public String getLengthFormatted() {
        int minutes = this.lengthInSeconds / 60;
        int seconds = this.lengthInSeconds % 60;
        return (minutes + ":" + seconds);
    }

    @Override
    public String toString() {
        return (this.title+ ", " + this.interpreter + ", " + this.lengthInSeconds + "sec");
    }

    public boolean isEpic() {
        return this.lengthInSeconds>200;
    }

}
