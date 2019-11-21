import javax.swing.*;
import java.awt.*;
@SuppressWarnings("serial")

public class P191121 extends JFrame {
	public P191121() {
		setTitle("201834957 지하윤 하트 버튼 그리기");
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Container contentPane = getContentPane();
		contentPane.setLayout(null); // 컨텐트팬의 배치관리자 제거
		//contentPane.setLayout(new GridLayout);
		
		int i, j, n=5;
		int x = 10;
		int y = 100;
		int a = 200;
		int b = 10;
		
		for(i=0;i<n;i++) {
			for(j=0;j<n;j++) {
				if(i==0&&(j>=n/5&&j<=n/2-n/5)||i==0&&(j>=n/2+n/5&&j<=(n-1)-n/5)) {
					x = x + 40;
					a = a + 20;
				}
				else if(i>0&&i<=n/5&&(j==n/5-i||j==n/2+n/5-i||j==n/2-n/5+i||j==(n-1)-n/5+i)) {
					x = x + 40;
					a = a + 20;
				}
				else if((i>n/5 &&i<=n/2)&&(j==0||j==n-1)) {
					x = x + 40;
					a = a + 20;
				}
				else if(i>n/2 &&(j==i-n/2||j==(n-1)-(i-n/2))) {
					x = x + 40;
					a = a + 20;
				}
				else {
					x = x + 40;
					a = a + 20;
					continue;
				}
				JLabel heart = new JLabel("♡");
				heart.setLocation(a, b);
				heart.setSize(20, 20);
				contentPane.add(heart);
				
				JButton but = new JButton("♥");
				but.setLocation(x, y);
				but.setSize(50, 20);
				contentPane.add(but);
			}
			y = y + 35;
			x = 10;
			b = b + 20;
			a = 200;
		}		
		setSize(500, 400);
		setVisible(true);
		}
	public static void main(String[] args) {
		new P191121();
		int i, j, n=5;
		for(i=0;i<n;i++) {
			for(j=0;j<n;j++) {
				if(i==0&&(j>=n/5&&j<=n/2-n/5)||i==0&&(j>=n/2+n/5&&j<=(n-1)-n/5))
					System.out.print("* ");
				else if(i>0&&i<=n/5&&(j==n/5-i||j==n/2+n/5-i||j==n/2-n/5+i||j==(n-1)-n/5+i))
					System.out.print("* ");
				else if((i>n/5 &&i<=n/2)&&(j==0||j==n-1))
					System.out.print("* ");
				else if(i>n/2 &&(j==i-n/2||j==(n-1)-(i-n/2)))
					System.out.print("* ");
				else System.out.print(" ");
				}
			System.out.print("\n");
		}
	}
}