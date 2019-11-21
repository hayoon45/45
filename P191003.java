import java.util.Scanner;
import java.util.InputMismatchException;
public class P191003 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int n1;
		int n2;
		Scanner Scan = new Scanner(System.in);
		while(true) {
			try {
				System.out.println("나뉨수를 입력하시오: ");		
				n1 = Scan.nextInt();
				}
			catch(InputMismatchException e) {
				System.out.println("정수가 아닙니다. 다시 입력하세요.");
				Scan.next();
				continue;
				}
			while(true) {
				try {
				System.out.println("나눗수를 입력하시오: ");
				n2 = Scan.nextInt();
				}
				catch(InputMismatchException e) {
					System.out.println("정수가 아닙니다. 다시 입력하세요.");
					Scan.next();
					continue;
				}
				try {
					System.out.println(n1 + "를" + n2 + "로 나누면 몫은" + n1/n2 + "입니다.");
				}
				catch(ArithmeticException e) {
					System.out.println("0으로 나눌 수 없습니다. 다른 정수를 입력하세요. ");
					continue;
				}
			break;
			}
		}
	}
}
