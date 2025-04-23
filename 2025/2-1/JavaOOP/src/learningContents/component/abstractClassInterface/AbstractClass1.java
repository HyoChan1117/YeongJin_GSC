package learningContents.component.abstractClassInterface;

// 추상 클래스에서 abstract를 붙일 수 있는 곳
// 1. 클래스 앞
// 2. 메서드 앞

// 미완성
// 추상 클래스의 성립 조건
abstract class Animal {
    // 추상 메서드 -> 미완성 메서드
    // 메서드의 정의만 기술 (함수의 반환형, 메서드 이름)
    // 구현부는 없음

    // 추상 메서드를 사용하면 강제성이 있음
    abstract void makeSound();
}

abstract class Dog extends Animal {
    // 부모에서 이미 추상
    void makeSound() {
        System.out.println("Dog");
    }
}

class Son extends Dog {
    void makeSound() {
        System.out.println("Son");
    }
}

public class AbstractClass1 {
    public static void main(String[] args) {

        Animal animal = new Son();
        animal.makeSound();

    }
}
