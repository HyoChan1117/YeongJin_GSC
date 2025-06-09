interface Test {
    void run() throws Exception;
}

class Bar implements Runnable {
    @Override
    public void run() {
        try {
            for (int i = 0; i < 10; i++) {
                System.out.println("* ");
                // 만약 예외 발생 가능성이 있는 코드가 있다면 여기에 위치
            }
        } catch (Exception e) {

        }
    }
}

class Foo implements Runnable {
    @Override
    public void run() {
        try {
            for (int i = 0; i < 10; i++) {
                System.out.println("_ ");
                // 만약 예외 발생 가능성이 있는 코드가 있다면 여기에 위치
            }
        } catch (Exception e) {

        }
    }
}

public class MainTest2 {
    public static void main(String[] args) {

        Bar bar = new Bar();
        Foo foo = new Foo();

        Thread myThread1 = new Thread(bar);
        Thread myThread2 = new Thread(foo);

        myThread1.start();
        myThread2.start();

    }
}
