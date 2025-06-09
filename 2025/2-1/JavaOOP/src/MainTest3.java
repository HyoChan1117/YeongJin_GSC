

public class MainTest3 {
    public static void main(String[] args) {
        // 구현되어 있는 추상 메서드를 구현하는데 사용
        // 한 번 사용할 클래스를 굳이 정의할 필요가 없을 때 사용
        // 이름이 없는 클래스를 사용하려면 다형성 이용해야 함
        // 1. 상속 : 부모 클래스에 정의해 놓은 메서드를 자식에서 재정의해서 사용하는 용도
        // 2. 인터페이스 : 인터페이스 내에서 정의해 놓은 추상 메서드를 구현하는 용도


        //           1) class 이름없음 extends Object {
        //              }
        //           2) new 이름없음();
        // 익명 클래스에 대한 정의
        Object obj = new Object() {

        };

        interface Test {};
        //           1) class 이름없음 implements Test {
        //              }
        //           2) new 이름없음();
        Test test = new Test() {};
    }
}
