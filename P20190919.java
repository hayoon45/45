import java.util.Scanner;
public class P20190919 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("원의 반지름, x좌표, y좌표를 정수의 형태로 빈칸으로 분리하여 입력하시오.");
		
		Scanner scanner = new Scanner(System.in);
		int r = scanner.nextInt();
		System.out.println("반지름은 "+r+"입니다.");
		int x = scanner.nextInt();
		System.out.println("x좌표는 "+x+"입니다.");
		int y = scanner.nextInt();
		System.out.println("y좌표는 "+y+"입니다.");
		
		scanner.close();
		
		double dis;
		dis = (r-x)*(r-x) + (r-y)*(r-y);
		int r2 = r*r;
		System.out.println(r2>dis);
	}

}
