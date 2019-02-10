import java.util.Scanner;

public class Game24 {

 /**
  * @param args
  */
 public static void main(String[] args) throws Exception {
  Scanner kb = new Scanner(System.in);
  while (true) {
   System.out.println("===== Game 24 Calculator =====");
   System.out.print(" How many numbers? : ");
   int i = kb.nextInt();
   double from[] = new double[i];
   for (; i > 0; i--) {
    System.out.print(" Enter the " + (from.length - i + 1));
    if (from.length - i + 1 == 1) {
     System.out.print("st");
    } else if (from.length - i + 1 == 2) {
     System.out.print("nd");
    } else if (from.length - i + 1 == 3) {
     System.out.print("rd");
    } else {
     System.out.print("th");
    }
    System.out.print(" number : ");
    from[from.length - i] = kb.nextDouble();
   }
   System.out.print(" Answer : ");
   double want = kb.nextDouble();
   new Game24(from, want);
   Thread.sleep(2000);
  }
 }

 private double answer = 0;

 public Game24(double[] numSet, double answer) {
  long initialTime = System.currentTimeMillis();
  this.answer = answer;
  System.out.print("Calculating...");
  Block out[] = this.doGame24(-1, -1, -1, numSet,
    new boolean[numSet.length]);
  System.out.print("\nCompleted in "
    + (System.currentTimeMillis() - initialTime)
    + " ms.\n Solution >> ");
  if (out != null) {
   for (int i = 0; i < out.length; i++) {
    if (out[i] != null) {
     System.out.print(out[i].toString(numSet));
    }
   }
   System.out.println();
  } else {
   System.out.println("### Unable to solve!");
  }
 }

 private Block[] doGame24(int index1, int findex, int index2,
   double numSet[], boolean deleted[]) {
  int numLeft = 0;
  double temp = 0;
  for (int i = 0; i < deleted.length; i++) {
   if (!deleted[i]) {
    temp = numSet[i];
    numLeft++;
   }
  }
  if (numLeft == 1) {
   if (Math.abs(temp - answer) < 1E-10) {
    return new Block[] { new Block(2, 0), new Block(0, index1),
      new Block(1, findex), new Block(0, index2),
      new Block(2, 1) };
   } else {
    return null;
   }
  }
  for (int f = 0; f < Game24.function.length; f++) {
   for (int i = 0; i < numSet.length; i++) {
    if (!deleted[i]) {
     for (int j = 0; j < numSet.length; j++) {
      if (!deleted[j]) {
       if (i != j) {

        double tempNumSet[] = numSet.clone();
        boolean tempDeleted[] = deleted.clone();
        tempDeleted[j] = true;
        if (f == 0) {
         tempNumSet[i] = plus(numSet[i], numSet[j]);
        } else if (f == 1) {
         tempNumSet[i] = minus(numSet[i], numSet[j]);
        } else if (f == 2) {
         tempNumSet[i] = multiply(numSet[i],
           numSet[j]);
        } else if (f == 3) {
         try {
          tempNumSet[i] = divide(numSet[i],
            numSet[j]);
         } catch (Exception e) {
          break;
         }
        }
        Block[] out = doGame24(i, f, j, tempNumSet,
          tempDeleted);
        if (out != null) {
         Block[] tempOut = new Block[out.length + 4];
         int tempOutLength = 0;
         for (int n = 0; n < out.length; n++) {
          if (out[n].type == 0
            && out[n].value == index1) {
           tempOut[tempOutLength++] = new Block(
             2, 0);
           tempOut[tempOutLength++] = new Block(
             0, index1);
           tempOut[tempOutLength++] = new Block(
             1, findex);
           tempOut[tempOutLength++] = new Block(
             0, index2);
           tempOut[tempOutLength++] = new Block(
             2, 1);
          } else {
           tempOut[tempOutLength++] = out[n];
          }
         }
         return tempOut;
        }

       }
      }
     }
    }
   }
  }

  return null;
 }

 private static double plus(double x1, double x2) {
  return x1 + x2;
 }

 private static double minus(double x1, double x2) {
  return x1 - x2;
 }

 private static double multiply(double x1, double x2) {
  return x1 * x2;
 }

 private static double divide(double x1, double x2) throws Exception {
  if (x2 == 0) {
   throw new Exception();
  }
  return x1 / x2;
 }

 /*
  * private static double sqrt(double x) throws Exception { return
  * Math.sqrt(x); }
  */
 protected static final String function[] = new String[] { "+", "-", "x",
   "/"/* , "sqrt" */};
 protected static final boolean function2v[] = new boolean[] { true, true,
   true, true /* , false */};
}

class Block {
 protected int type;
 protected int value;

 protected Block(int type, int value) {
  this.type = type;
  this.value = value;
 }

 protected String toString(double[] numSet) {
  if (this.type == 0) {
   if (numSet[this.value] == Math.floor(numSet[this.value])) {
    return (int) numSet[this.value] + "";
   }
   return numSet[this.value] + "";
  } else if (this.type == 1) {
   return Game24.function[this.value];
  } else if (this.type == 2) {
   if (this.value == 0) {
    return "(";
   }
   return ")";
  }
  return "";
 }
}﻿