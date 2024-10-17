package LearningContents.Operator.BitwiseOperator;

public class BitwiseOperator1 {
    public static void main(String[] args) {

        int myIpAddr = 0xD265ECA4;

        // >> 와 & 연산자를 조합해서 IPv4 각 자리수를 각 int 형 변수 ipAddr에 저장
        int ipAdr1 = (myIpAddr >> 24) & 0xFF;
        int ipAdr2 = (myIpAddr >> 16) & 0xFF;
        int ipAdr3 = (myIpAddr >> 8) & 0xFF;
        int ipAdr4 = myIpAddr & 0xFF;

        System.out.println(ipAdr1 + "." + ipAdr2 + "." + ipAdr3 + "." + ipAdr4);
    }
}
