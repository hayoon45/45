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
				System.out.println("�������� �Է��Ͻÿ�: ");		
				n1 = Scan.nextInt();
				}
			catch(InputMismatchException e) {
				System.out.println("������ �ƴմϴ�. �ٽ� �Է��ϼ���.");
				Scan.next();
				continue;
				}
			while(true) {
				try {
				System.out.println("�������� �Է��Ͻÿ�: ");
				n2 = Scan.nextInt();
				}
				catch(InputMismatchException e) {
					System.out.println("������ �ƴմϴ�. �ٽ� �Է��ϼ���.");
					Scan.next();
					continue;
				}
				try {
					System.out.println(n1 + "��" + n2 + "�� ������ ����" + n1/n2 + "�Դϴ�.");
				}
				catch(ArithmeticException e) {
					System.out.println("0���� ���� �� �����ϴ�. �ٸ� ������ �Է��ϼ���. ");
					continue;
				}
			break;
			}
		}
	}
}
