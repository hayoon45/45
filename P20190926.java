import java.util.Scanner;
public class P20190926 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
		System.out.println("�������� �Է��Ͻÿ�: ");
		Scanner scan = new Scanner(System.in);
		int num1 = scan.nextInt();
		
		System.out.println("�Է��� ���� ���������� " + Integer.toBinaryString(num1) + "�̴�.");
		
		System.out.println("�˰����ϴ� bit�� ��ġ�� �Է��Ͻÿ�(���������κ��� 1~4����): ");
		
		int i = scan.nextInt();
		int j = (num1 >>> (i-1));
		int x = (j & 00000001);
		
		if (x == 0) {
			System.out.println(i + "��° ��ġ�� bit��  0�Դϴ�.");
		}
		else {
			System.out.println(i + "��° ��ġ�� bit��  1�Դϴ�.");
		}
		
		scan.close();
	}

}
