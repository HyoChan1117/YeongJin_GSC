package learningContents.component.nestedClass;

class Board {
    // Outer class에 있는 멤버들은 static nested class에서 사용할 수 있음
    // int x = 0; -> Display 클래스에서 사용 못함 : Display 클래스는 static 중첩 클래스이기 때문
    // static int x = 0; -> Display 클래스에서 사용 가능

    static class Display {
        static void prt() {
            System.out.println("Display");
        }
    }

    static class Pagination {
        static int getCurrentPage() { return 0; }
    }
}

public class test1 {
    public static void main(String[] args) {
        Board.Display.prt();
        Board.Pagination.getCurrentPage();
    }
}
