import java.util.Scanner;
public class P20190919 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("���� ������, x��ǥ, y��ǥ�� ������ ���·� ��ĭ���� �и��Ͽ� �Է��Ͻÿ�.");
		
		Scanner scanner = new Scanner(System.in);
		int r = scanner.nextInt();
		System.out.println("�������� "+r+"�Դϴ�.");
		int x = scanner.nextInt();
		System.out.println("x��ǥ�� "+x+"�Դϴ�.");
		int y = scanner.nextInt();
		System.out.println("y��ǥ�� "+y+"�Դϴ�.");
		
		scanner.close();
		
		double dis;
		dis = (r-x)*(r-x) + (r-y)*(r-y);
		int r2 = r*r;
		System.out.println(r2>dis);
	}

}
