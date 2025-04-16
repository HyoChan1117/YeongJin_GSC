package lab.carBrand;

// Car2 클래스 정의
class Car2 {
    // 인스턴스 멤버 변수: 각 자동차 객체의 브랜드와 속도를 저장
    String brand; // 자동차 브랜드
    int speed;    // 자동차 속도
}

public class Lab2 {
    public static void main(String[] args) {
        // 객체 생성
        // Heap 영역에 Car2 객체가 생성되고, Stack 영역의 변수 car가 이를 참조
        // 생성한 객체를 사용하기 위해 Heap에 저장된 객체를, Stack에 있는 참조변수 이를 참조
        Car2 car = new Car2();

        // 참조 변수를 통해 인스턴스 멤버 변수에 값 할당
        car.brand = "BMW";
        car.speed = 100;

        // 참조 변수를 이용해 인스턴스 멤버 변수 값 Get
        System.out.println("브랜드: " + car.brand + ", 속도: " + car.speed);
    }
}
