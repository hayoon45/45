import java.util.Scanner;
public class P191010 {
	String title, author, year;
	public P191010(String title, String author, String year) {
		this.title = title;
		this.author = author;
		if (year.equals("0")) {
			this.year = "발간년도미상";
		}
		else this.year = year;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		P191010 [] book;
		book = new P191010[2];
		
		Scanner scan = new Scanner(System.in);
		for(int i=0; i<book.length; i++) {
			System.out.print("제목>>");
			String title = scan.nextLine();
			System.out.print("저자>>");
			String author = scan.nextLine();
			System.out.print("발간년도>>");
			String year = scan.nextLine();

			book[i] = new P191010(title, author, year);
		}
		
		for(int i=0; i<book.length; i++) {
			System.out.print("(" + book[i].title + ", " + book[i].author + ", " + book[i].year + ")");
		}
		
		scan.close();
	}
}
