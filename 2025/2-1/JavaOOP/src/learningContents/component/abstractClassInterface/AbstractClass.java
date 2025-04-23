package learningContents.component.abstractClassInterface;

// 추상 클래스에서 abstract를 붙일 수 있는 곳
// 1. 클래스 앞
// 2. 메서드 앞

// 미완성
// 추상 클래스의 성립 조건
abstract class Pos {
    // 추상 메서드 -> 미완성 메서드
    // 메서드의 정의만 기술 (함수의 반환형, 메서드 이름)
    // 구현부는 없음
    abstract void prt();
}


public class AbstractClass {
    public static void main(String[] args) {

        // 추상 클래스로는 객체를 생성할 수 없음
//        Pos p = new Pos();

    }
}
