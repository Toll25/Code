package com.company;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class RechteckTest {

    @Test
    void constructor(){
        Rechteck rechteck = new Rechteck(5,6,"#FF00FF", false);
        assertEquals(5, rechteck.getA());
        assertEquals(6, rechteck.getB());
        assertFalse(rechteck.isVisible());
    }

    @Test
    void calculateArea() {
        Rechteck rechteck = new Rechteck (3, 7, "#FF00FF", false);
        assertEquals(21, rechteck.calculateArea());
    }

    @Test
    void testToString() {
        // <a> x <b>;<color>;<isVisible>, z.B. 4 x 3;#7F7F7F;false
        Rechteck rechteck = new Rechteck(5,5,"#FF00FF", false);
        String test= "5 x 5;#FF00FF;false";
        assertEquals(test,rechteck.toString());
    }

    @Test
    void valueOf() {
        Rechteck rechteck= Rechteck.valueOf("5 x 6;#FF00FF;false");
        assertEquals(new Rechteck(5,6,"#FF00FF",false), rechteck);
    }

    @Test
    void testEquals_SameInstance() {
        Rechteck rechteck=new Rechteck(5,6,"#FF00FF",false);
        assertTrue(rechteck.equals(rechteck));
    }

    @Test
    void testEquals_DiffClass() {
        Rechteck rechteck=new Rechteck(5,6,"#FF00FF",false);
        assertFalse(rechteck.equals("irgendeinString"));
    }

    @Test
    void testEquals_DiffA(){
        Rechteck rechteck1=new Rechteck(4,6,"#FF00FF",false);
        Rechteck rechteck2=new Rechteck(5,6,"#FF00FF",false);
        assertFalse(rechteck1.equals(rechteck2));
    }

    @Test
    void testEquals_SameA() {
        Rechteck rechteck1=new Rechteck(5,6,"#FF00FF",false);
        Rechteck rechteck2=new Rechteck(5,6,"#FF00FF",false);
        assertTrue(rechteck1.equals(rechteck2));
    }

    @Test
    void testEquals_DiffB() {
        Rechteck rechteck1=new Rechteck(5,7,"#FF00FF",false);
        Rechteck rechteck2=new Rechteck(5,6,"#FF00FF",false);
        assertFalse(rechteck1.equals(rechteck2));
    }

    @Test
    void testEquals_SameB() {
        Rechteck rechteck1=new Rechteck(5,6,"#FF00FF",false);
        Rechteck rechteck2=new Rechteck(5,6,"#FF00FF",false);
        assertTrue(rechteck1.equals(rechteck2));
    }

    @Test
    void testEquals_DiffColor() {
        Rechteck rechteck1=new Rechteck(5,6,"#FF00FF",false);
        Rechteck rechteck2=new Rechteck(5,6,"#FF10FF",false);
        assertFalse(rechteck1.equals(rechteck2));
    }

    @Test
    void testEquals_SameColor() {
        Rechteck rechteck1=new Rechteck(5,6,"#FF00FF",false);
        Rechteck rechteck2=new Rechteck(5,6,"#FF00FF",false);
        assertTrue(rechteck1.equals(rechteck2));
    }

    @Test
    void testEquals_DiffIsVisible() {
        Rechteck rechteck1=new Rechteck(5,6,"#FF00FF",false);
        Rechteck rechteck2=new Rechteck(5,6,"#FF00FF",true);
        assertFalse(rechteck1.equals(rechteck2));
    }

    @Test
    void testEquals_SameIsVisible() {
        Rechteck rechteck1=new Rechteck(5,6,"#FF00FF",false);
        Rechteck rechteck2=new Rechteck(5,6,"#FF00FF",false);
        assertTrue(rechteck1.equals(rechteck2));
    }

    @Test
    void testEquals_DiffInstanceSameValues() {
        Rechteck rechteck1 = new Rechteck(123,321,"FFFFFFF", true);
        Rechteck rechteck2 = new Rechteck(123,321,"FFFFFFF", true);
        assertTrue(rechteck1.equals(rechteck2));
        assertEquals(rechteck1.getA(),rechteck2.getA());
        assertEquals(rechteck1.getB(),rechteck2.getB());
        assertEquals(rechteck1.getColor(),rechteck2.getColor());
        assertEquals(rechteck1.isVisible(),rechteck2.isVisible());
    }

    @Test
    void compareTo() {
        Rechteck rechteck1 = new Rechteck(5, 6, "#FF00FF", true);
        Rechteck rechteck2 = new Rechteck(5, 6, "#FF00F0", false);
        assertEquals(1, rechteck1.compareTo(rechteck2));
    }
    @Test
    void compareTo_diffArea() {
        Rechteck rechteck1 = new Rechteck(5, 6, "#FF00FF", false);
        Rechteck rechteck2 = new Rechteck(6, 3, "#FF00FF", false);
        assertEquals(12, rechteck1.compareTo(rechteck2));
    }
    @Test
    void compareTo_diffColor() {
        Rechteck rechteck1 = new Rechteck(5, 6, "#FF00FA", false);
        Rechteck rechteck2 = new Rechteck(5, 6, "#FF00FF", false);
        assertEquals(-5, rechteck1.compareTo(rechteck2));
    }
    @Test
    void compareTo_diffBoolean() {
        Rechteck rechteck1 = new Rechteck(5, 6, "#FF00FF", true);
        Rechteck rechteck2 = new Rechteck(5, 6, "#FF00FF", false);
        assertEquals(1, rechteck1.compareTo(rechteck2));
    }
    @Test
    void compareTo_diffArea_and_diffColor() {
        Rechteck rechteck1 = new Rechteck(5, 8, "#FF00FF", false);
        Rechteck rechteck2 = new Rechteck(4, 8, "#FF00F0", false);
        assertEquals(8, rechteck1.compareTo(rechteck2));
    }
    @Test
    void compareTo_diffArea_and_diffBool() {
        Rechteck rechteck1 = new Rechteck(7, 6, "#FF00FF", true);
        Rechteck rechteck2 = new Rechteck(5, 6, "#FF00FF", false);
        assertEquals(1, rechteck1.compareTo(rechteck2));
    }
    @Test
    void compareTo_diffB_and_diffBool() {
        Rechteck rechteck1 = new Rechteck(5, 7, "#FF00FF", true);
        Rechteck rechteck2 = new Rechteck(5, 5, "#FF00F0", false);
        assertEquals(1, rechteck1.compareTo(rechteck2));
    }
    @Test
    void compareTo_diffColor_and_diffBool() {
        Rechteck rechteck1 = new Rechteck(5, 5, "#FF00FF", true);
        Rechteck rechteck2 = new Rechteck(5, 5, "#FF00F0", false);
        assertEquals(1, rechteck1.compareTo(rechteck2));
    }
    @Test
    void compareTo_diffArea_and_diffColor_and_diffBool(){
        Rechteck rechteck1 = new Rechteck(5, 4, "#FF00FF", true);
        Rechteck rechteck2 = new Rechteck(4, 6, "#FF00F0", false);
        assertEquals(1, rechteck1.compareTo(rechteck2));
    }

}