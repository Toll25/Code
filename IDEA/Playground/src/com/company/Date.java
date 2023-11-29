package com.company;

import java.util.Objects;

public class Date implements Comparable<Date> {
    private int year;
    private int month;
    private int day;

    public Date(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        this.month = month;
    }

    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        this.day = day;
    }

    @Override
    public String toString() {
        return (year + " - " + month + " - " + day);
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        if (other == null || getClass() != other.getClass()) return false;
        Date date = (Date) other;
        return year == date.year && month == date.month && day == date.day;
    }

    @Override
    public int compareTo(Date other) {
        if (this.year == other.year) {
            if (this.month == other.month) {
                if (this.day == other.day) {

                }else{
                    return this.day - other.day;
                }

            }else{
                return this.month-other.month;
            }

        }else{
            return this.year-other.year;
        }
        return 0;
    }
}