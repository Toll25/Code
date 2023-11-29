public class EnumExample {
    public enum Color {
        WHITE, BLACK, GREY
    }

    public static void main(String[] args) {

        Color[][] array = {
                {Color.WHITE, Color.BLACK, Color.BLACK, Color.BLACK},
                {Color.WHITE, Color.WHITE, Color.BLACK, Color.BLACK},
                {Color.WHITE, Color.BLACK, Color.GREY, Color.BLACK},
                {Color.BLACK, Color.GREY, Color.GREY, Color.GREY}
        };
        for (Color[] ints : array) {
            for (Color anInt : ints) {
                switch (anInt) {
                    case BLACK -> System.out.print("*  ");
                    case GREY -> System.out.print(".  ");
                    case WHITE -> System.out.print("   ");
                }
            }
            System.out.println();
        }
    }
}
