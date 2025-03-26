package Lab.component.classObjectInstance;

// 클래스: 객체를 생성하기 위한 설계도 (붕어빵 틀)
// 인스턴스: 클래스로부터 생성된 객체가 메모리에 할당 된 상태 (붕어빵)


class Car1 {
    // 인스턴스 멤버 변수: 각 자동차 객체마다 고유한 브랜드와 속도 정보를 가짐
    String brand; // 자동차 브랜드
    int speed;    // 자동차 속도

    // 인스턴스 멤버 메서드: 자동차의 브랜드와 속도 정보를 출력
    void infoCar() {
        System.out.println("브랜드: " + brand + ", 속도: " + speed);
    }
}

public class Lab1 {
    public static void main(String[] args) {
        // Car1 클래스의 인스턴스 생성
        Car1 car = new Car1();

        // car 인스턴스의 멤버 변수에 값 할당
        car.brand = "BMW";
        car.speed = 100;

        // car 인스턴스의 메서드 호출
        car.infoCar(); // 출력: 브랜드: BMW, 속도: 100
    }
}
