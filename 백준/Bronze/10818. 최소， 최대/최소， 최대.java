import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int a = Integer.parseInt(br.readLine());
    StringTokenizer st = new StringTokenizer(br.readLine()," ");
    int max = Integer.MIN_VALUE;
    int min = Integer.MAX_VALUE;

    while(st.hasMoreTokens()) {
      int val = Integer.parseInt(st.nextToken());
      if (val > max) {
        max = val;
      }
      if (val < min) {
        min = val;
      }
    }
    System.out.println(min + " " + max);
  }
}