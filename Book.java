import java.util.Scanner;
public class Book {
	String title, author, year;
	public Book(String title, String author, String year) {
		this.title = title;
		this.author = author;
		this.year = year;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Book [] book;
		book = new Book[2];
		
		Scanner scan = new Scanner(System.in);
		for(int i=0; i<book.length; i++) {
			System.out.print("����>>");
			String title = scan.nextLine();
			System.out.print("����>>");
			String author = scan.nextLine();
			System.out.print("�߰��⵵>>");
			String year = scan.nextLine();
			if (year.equals("0")) {
				year = "�߰��⵵�̻�";
			}
			book[i] = new Book(title, author, year);
		}
		
		for(int i=0; i<book.length; i++) {
			System.out.print("(" + book[i].title + ", " + book[i].author + ", " + book[i].year + ")");
		}
		
		scan.close();

	}

}
