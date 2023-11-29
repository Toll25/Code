package ChristmasTree;

public class Main {

    public static void main(String[] args) {
        Decoration decoration = new Decoration(10, '*');
	    Tree tree = new Tree(100,'M',decoration);
        tree.draw();
    }
}
