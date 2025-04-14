package learningContents.component.inheritance.overriding;


class Player {
    void shoot() { System.out.println("슛");}
}
class Sg extends Player {
    void shoot() { System.out.println("슈팅가드 슛");}
}
class Pg extends Player {
    void shoot() { System.out.println("포인트 슛");}
}
class C extends Player {
    void shoot() { System.out.println("센터 슛");}
}
class Pf extends Player {
    void shoot() { System.out.println("파워포워드 슛");}
}
class Sf extends Player {
    void shoot() { System.out.println("스몰포워드 슛");}
}
public class Overriding1 {
    public static void main(String[] args) {

//        C c = new C();
//        Sg sg = new Sg();
//        Pg pg = new Pg();
//        Sf sf = new Sf();
//        Pf pf = new Pf();

        Player p[] = new Player[5];
        p[0] = new C();
        p[1] = new Sg();
        p[2] = new Pg();
        p[3] = new Sf();
        p[4] = new Pf();

        for (int i = 0; i < 5; i++) {
            p[i].shoot();
        }

    }
}
