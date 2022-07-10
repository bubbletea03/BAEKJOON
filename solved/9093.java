import java.util.Scanner;

class Main {
    public static void main(String[] args) throws Exception {
        
        // 입력
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();
        String[] str = new String[n];
        for(int i=0; i<n; i++){
            str[i] = scanner.nextLine();
        }
        scanner.close();

        String[][] word = new String[n][];
        for(int i=0; i<n; i++){
            word[i] = str[i].split(" ");
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<word[i].length; j++){
                System.out.print(get_reversedString(word[i][j])+" ");
            }
            System.out.println();
        }
    }

    static String get_reversedString(String str){
        int len = str.length();
        char[] reversedCharArr = new char[len];
        for(int i=0; i<len; i++){
            reversedCharArr[i] = str.charAt(len-i-1);
        }

        return new String(reversedCharArr);
    }
}
