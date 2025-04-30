package learningContents.component.polymorphism;

// 공통 부모 클래스
class Player1 {
    protected String name;
    protected String position;

    Player1(String name, String position) {
        this.name = name;
        this.position = position;
    }

    public void shoot() {
        System.out.println(position + " " + name + ": 기본 슛");
    }
}

class Sg1 extends Player1 {
    Sg1(String argName) {
        super(argName, "슈팅 가드");
    }

    @ Override
    public void shoot() {
        System.out.println(position + " " + name + ": 3점슛!");
    }
}

class Pg1 extends Player1 {
    Pg1(String argName) {
        super(argName, "포인트 가드");
    }

    @Override
    public void shoot() {
        System.out.println(position + " " + name + ": 돌파 후 점퍼!");
    }
}

class Center1 extends Player1 {
    Center1(String argName) {
        super(argName, "센터");
    }

    @Override
    public void shoot() {
        System.out.println(position + " " + name + ": 골밑슛!");
    }
}

class Pf1 extends Player1 {
    Pf1(String argName) {
        super(argName, "파워 포워드");
    }

    @Override
    public void shoot() {
        System.out.println(position + " " + name + ": 미들슛!");
    }
}

class Sf1 extends Player1 {
    Sf1(String argName) {
        super(argName, "스몰 포워드");
    }


}

public class Polymorphism1 {
}
