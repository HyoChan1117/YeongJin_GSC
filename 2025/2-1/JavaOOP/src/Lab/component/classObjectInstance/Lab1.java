package Lab.component.classObjectInstance;

// 클래스 - 객체를 생성하기 위한 설계도 (붕어빵 틀)
// 메모리 할당 시점(위치)프로그램 시작 시 클래스 로더에 의해 메모리의 메소드 영역에 로드됨 - Method Area
// 용도: 객체 생성을 위한 설계

// 객체 -

// 인스턴스: 클래스로부터 생성된 객체가 메모리에 할당 된 상태 (붕어빵)
// new 연산자를 통해 객체가 생성될 때 - Heap(힙 영역)
// 용도: 클래스를 바탕으로 만든 실제로 사용되는 객체

class Car1 {
    // 인스턴스 멤버 변수
    String brand; // 자동차 브랜드
    int speed;    // 자동차 속도

    // 인스턴스 멤버 메서드
    void infoCar() {
        System.out.println("브랜드: " + brand + ", 속도: " + speed);
    }
}

public class Lab1 {
    public static void main(String[] args) {
        // 객체 생성
        Car1 car = new Car1();

        // 참조변수를 이용하여 인스턴스 변수 값 할당
        car.brand = "BMW";
        car.speed = 100;

        // 인스턴스의 메서드 호출
        car.infoCar(); // 출력: 브랜드: BMW, 속도: 100
    }
}
