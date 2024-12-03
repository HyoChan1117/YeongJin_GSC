import org.w3c.dom.ls.LSOutput;

public class test {
    static int[] getSumAvg(int argA, int argB) {
        int sum = argA + argB;
        int avg = sum / 2;

        // sum, avg
        int[] retValue = {sum, avg};

        return retValue;
    }

    public static void main(String[] args) {
        System.out.println(getSumAvg(1, 2));
    }
}
