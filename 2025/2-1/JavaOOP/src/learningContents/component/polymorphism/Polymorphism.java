package learningContents.component.polymorphism;

// 부모 클래스
class Animal {
    void sound() {
        System.out.println("동물이 소리를 냅니다.");
    }
}

// 자식 클래스 1
class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("멍멍!");
    }
}

// 자식 클래스 2
class Cat extends Animal {
    @Override
    void sound() {
        System.out.println("야옹~");
    }
}

// 실행 클래스
public class Polymorphism {
    public static void main(String[] args) {
        // 부모 타입 배열에 자식 객체들을 저장
        Animal[] animals = new Animal[3];
        animals[0] = new Animal();  // 동물
        animals[1] = new Dog();     // 강아지
        animals[2] = new Cat();     // 고양이

        // 반복문으로 다형성 확인
        for (Animal a : animals) {
            a.sound();  // 각 객체의 오버라이딩된 sound() 실행
        }
    }
}
