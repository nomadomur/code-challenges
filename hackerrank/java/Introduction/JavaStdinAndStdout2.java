package Introduction;
import java.util.Scanner;

public class JavaStdinAndStdout2 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int s = scan.nextInt();
        double d = scan.nextDouble();
        scan.nextLine();
        String i = scan.nextLine();

        System.out.println("String: " + i);
        System.out.println("Double: " + d);
        System.out.println("Int: " + s);
    }
}