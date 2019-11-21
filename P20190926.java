import java.util.Scanner;
public class P20190926 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
		System.out.println("십진수를 입력하시오: ");
		Scanner scan = new Scanner(System.in);
		int num1 = scan.nextInt();
		
		System.out.println("입력한 수의 이진수형은 " + Integer.toBinaryString(num1) + "이다.");
		
		System.out.println("알고자하는 bit의 위치를 입력하시오(오른쪽으로부터 1~4까지): ");
		
		int i = scan.nextInt();
		int j = (num1 >>> (i-1));
		int x = (j & 00000001);
		
		if (x == 0) {
			System.out.println(i + "번째 위치의 bit는  0입니다.");
		}
		else {
			System.out.println(i + "번째 위치의 bit는  1입니다.");
		}
		
		scan.close();
	}

}
