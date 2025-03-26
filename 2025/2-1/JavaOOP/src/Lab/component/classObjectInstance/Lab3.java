package Lab.component.classObjectInstance;

// 자동차 클래스를 정의
class Car3 {
    // 클래스 멤버 변수 (모든 인스턴스가 공유)
    static int totalCars = 0;

    // 인스턴스 멤버 변수 (각 객체마다 별도 존재)
    String brand;
    int speed;

    // 클래스 초기화 블록: 클래스가 처음 로딩될 때 한 번 실행
    static {
        System.out.println("자동차에 대한 정보");
    }

    // 인스턴스 초기화 블록: 객체가 생성될 때마다 생성자보다 먼저 실행됨
    {
        System.out.println("자동차 정보 생성");
    }

    // Default 생성자 - 매개변수 없음
    Car3() {
    }

    // Parameter 생성자 - 매개변수로 브랜드와 속도를 설정
    Car3(String brand, int speed) {
        this.brand = brand;
        this.speed = speed;
        totalCars++; // 생성될 때마다 총 자동차 수 증가
    }

    // 클래스 멤버 메서드: 클래스 이름으로 호출 가능
    static void showTotalCars() {
        System.out.println("총 자동차 수: " + totalCars);
    }

    // 인스턴스 멤버 메서드: 객체를 통해 호출
    void drive() {
        System.out.println("브랜드: " + brand + ", 속도: " + speed + "km/h");
    }
}

public class Lab3 {
    public static void main(String[] args) {
        // 자동차 객체 생성
        Car3 car1 = new Car3();  // Default 생성자 호출
        Car3 car2 = new Car3("BMW", 100);  // Parameter 생성자 호출

        // 객체의 참조변수를 이용해 인스턴스 멤버 메서드 접근 - 자동차 주행 정보 출력
        car2.drive();

        // 클래스의 생성된 자동차의 총 개수 출력
        Car3.showTotalCars();
    }
}
