package learningContents.component.abstractClassInterface;

abstract class Player {
    String name;

    Player(String argName) {
        this.name = argName;
    }

    // 모든 포지션에 공통적으로 필요한 메서드
    void introduce() {
        System.out.println("Hi, I'm " + name);
    }

    // 추상 메서드 : 각 포지션마다 다르게 동작해야 함
    abstract void play();  // 반드시 자식이 구현해야 함
}

class PG extends Player {
    PG(String argName) {
        super(argName);
    }

    @Override
    void play() {
        System.out.println(name + " is making assists as a Point Guard.");
    }
}

class SG extends Player {
    SG(String argName) {
        super(argName);
    }

    @Override
    void play() {
        System.out.println(name + " is shooting 3-pointers as a Shooting Guard.");
    }
}

class SF extends Player {
    SF(String argName) {
        super(argName);
    }

    @Override
    void play() {
        System.out.println(name + " is driving to the basket as a Small Forward.");
    }
}

class PF extends Player {
    PF(String argName) {
        super(argName);
    }

    @Override
    void play() {
        System.out.println(name + " is boxing out as a Power Forward.");
    }
}

class C extends Player {
    C(String argName) {
        super(argName);
    }

    @Override
    void play() {
        System.out.println(name + " is defending the paint as a Center.");
    }
}



public class BasketballGame {
    public static void main(String[] args) {

        Player[] team = {
                new PG("Chris"),
                new SG("Ray"),
                new SF("Paul"),
                new PF("Kevin"),
                new C("Dwight")
        };

        for (Player p : team) {
            p.introduce();
            p.play();
            System.out.println();
        }
    }
}