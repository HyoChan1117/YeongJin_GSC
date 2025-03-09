class Car2 {
    // static 변수 (Method Area에 저장됨)
    static int totalCars = 0;

    // 인스턴스 변수 (Heap에 저장됨)
    String brand;
    int speed;

    // 생성자
    public Car2(String brand) {
        this.brand = brand;
        this.speed = 0;
        totalCars++;  // 클래스 변수 증가
    }

    // 인스턴스 메서드 (Stack에서 호출됨)
    public void accelerate() {
        speed += 10;
        System.out.println(brand + " 속도: " + speed + "km/h");
    }

    // 정적 메서드 (Method Area에 저장됨)
    public static void showTotalCars() {
        System.out.println("총 자동차 개수: " + totalCars);
    }
}

public class classObject {
    public static void main(String[] args) {
        // main() 메서드는 Stack에 저장됨

        // 객체 생성 (Heap에 저장됨, 참조 변수는 Stack에 저장)
        Car2 car1 = new Car2("Toyota");  // car1 -> Heap의 객체 참조
        Car2 car2 = new Car2("BMW");     // car2 -> Heap의 객체 참조

        // 인스턴스 메서드 호출 (Stack에서 실행)
        car1.accelerate();  // Toyota 속도: 10km/h
        car2.accelerate();  // BMW 속도: 10km/h

        // 정적 메서드 호출 (Method Area에서 실행)
        Car2.showTotalCars();  // 총 자동차 개수: 2
    }
}
