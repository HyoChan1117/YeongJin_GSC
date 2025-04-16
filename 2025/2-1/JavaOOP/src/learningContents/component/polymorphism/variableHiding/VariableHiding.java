package learningContents.component.polymorphism.variableHiding;

// Player 클래스: 기본적인 슛 기능을 가진 부모 클래스
class Player1 {
    void shoot() {
        System.out.println("슛");  // 기본 슛 출력
    }
}

// Sg 클래스: Player 클래스를 상속받아 shoot() 메서드를 오버라이딩
class Sg1 extends Player1 {
    void shoot() {
        System.out.println("가드 슛");  // 가드 슛 출력
    }
}

// Pg 클래스: Player 클래스를 상속받아 shoot() 메서드를 오버라이딩
class Pg1 extends Player1 {
    void shoot() {
        System.out.println("포인트 가드 슛");  // 포인트 가드 슛 출력
    }
}

public class VariableHiding {
    public static void main(String[] args) {
        // 다형성(polymorphism) 예시
        // 부모 클래스 타입의 배열을 선언하면 다양한 자식 객체를 저장할 수 있다
        Player1 p[] = new Player1[2];  // Player 타입의 배열 생성

        // 각각의 배열 요소에 자식 클래스의 객체를 할당
        p[0] = new Sg1();  // 첫 번째는 Sg1 객체
        p[1] = new Pg1();  // 두 번째는 Pg1 객체

        // 반복문을 통해 각 객체의 shoot() 메서드를 호출
        // 오버라이딩된 메서드가 실행됨 → 자식 클래스의 메서드가 실행된다
        for (int i = 0; i < p.length; i++) {
            p[i].shoot();  // 실제 객체 타입에 따라 다른 출력이 나옴
        }
    }
}
