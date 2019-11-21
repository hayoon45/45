
public class P20191023 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		byte d = -8;
		short a = (short)0x55ff;
		short b = (short)0x00ff;
		System.out.printf("%04x\n", (a&b));
		System.out.printf("%x\n", (d>>2));
		System.out.printf("%x\n", (d>>>2));
	}

}
