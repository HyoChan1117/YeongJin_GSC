package learningContents.component.nestedClass.encapsulation;

class Bar {
    // private Inner Class는 외부에 노출하지 않고 오직 Bar 클래스 내부에서만 사용하기 위한 캡슐화 용도
    private class Foo {
    }
}

public class capsule {
    public static void main(String[] args) {
        Bar b = new Bar();

//        Bar.Foo f = b.new Foo();  b.new Foo()를 호출하면 컴파일 오류 발생 -> Foo 클래스가 private이기 때문

    }
}
