package learningContents.component.nestedClass.staticNestedClass;

class Board {
    // Outer class에 있는 static 멤버들은 static nested class에서 사용할 수 있음
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

public class Study1 {
    public static void main(String[] args) {
        // Outer 클래스의 객체 없이도 접근 가능 -> static Nested Class 이기 때문
        Board.Display.prt();
        System.out.println(Board.Pagination.getCurrentPage());
    }
}
