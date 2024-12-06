import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;


public class StudentGrade {
	static double[][] totalDatabase;
	static ArrayList<Double> position;

public static int getPosition(double[][] totalDatabase, double currentTotal) {
	position = new ArrayList<>();
	for (int i = 0; i < totalDatabase.length; i++) {
		position.add(totalDatabase[i][0]);
			}
	Collections.sort(position);
	Collections.reverse(position);
	
	int actualPosition = (position.indexOf(currentTotal) + 1);
	return actualPosition;
	}


public static double getHighest (double[][] database, int index) {

	double largest = database[0][index];
	for (int i = 0; i < database.length; i++){
		if (largest <= database[i][index]) largest = database[i][index];
		}
	return largest;
	}

	public static void main (String[] args) {

	Scanner scanner = new Scanner(System.in);

	System.out.println("How many students do you have?"); 
	int studentMean = scanner.nextInt();

	System.out.println("How many subjects do they offer?"); 
	int subjectMean = scanner.nextInt();
	String loadMmemonic = """ 

	Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>>
	Saved successfully
	""";
	System.out.println(loadMmemonic);

	int[][] database = new int [studentMean][subjectMean];
	totalDatabase = new double [studentMean][1];


	for(int i = 0 ; i <= studentMean; i++){
		if ( i >= studentMean) continue;
		for(int j = 0 ; j <= subjectMean; j++){
		if ( j >= subjectMean) continue;
		System.out.println("\033[H\033[2J");
        	System.out.flush();

		System.out.println(loadMmemonic);
		System.out.println("Entering score for student "+( i + 1) + "\n" + " Enter score for subject"+ (j + 1));
		database[i][j] = scanner.nextInt();
		totalDatabase[i][0] += database[i][j];
			}
	}
	
	System.out.println("\033[H\033[2J");
        	System.out.flush();


	System.out.println("====================================================================");
	System.out.printf("STUDENT %-7s", "");

	for(int j = 0 ; j <= subjectMean; j++){
	if ( j >= subjectMean) continue;
	System.out.printf("SUB" + (j  + 1) + "%-4s", "" );
		}
		
	System.out.printf("TOT %-4s AVE %-7s POS%n", "", "");
	System.out.println("====================================================================");
	
	for(int i = 0 ; i <= studentMean; i++){
		
		if ( i >= studentMean) continue;
		System.out.printf("%n");
		System.out.printf("Student "+( i + 1) + "%-7s", "");
			for(int j = 0 ; j <= subjectMean; j++){
				if ( j >= subjectMean) continue;
				System.out.printf((database[i][j]) + "%-6s", "");
				}
		System.out.printf((totalDatabase[i][0]) + "%-6s", "" );
		System.out.printf(((totalDatabase[i][0]) / 2) + "%-6s", "" );
		System.out.printf("%-1s%s","",getPosition(totalDatabase, totalDatabase[i][0]));
		
		}
	
	 
	System.out.print("""
\n
====================================================================
====================================================================
""");
		
			
	for(int i = 0 ; i <= studentMean; i++){
		if ( i >= studentMean) continue;
		System.out.printf("SUBJECT SUMMARY%n");
		for(int j = 0 ; j <= subjectMean; j++){
		if ( j >= subjectMean) continue;

	 /**for (int j = 0; j < subjectMean; j++) {
            System.out.printf("Subject %d%n", j + 1);
            double highestScore = getHighest(database, j);
            int highestStudent = 0;
            for (int i = 0; i < studentMean; i++) {
                if (database[i][j] == highestScore) {
                    highestStudent = i + 1;
                    break;

		
		System.out.println("Subject " + (j + 1));
		System.out.printf("Highest Scoring Student is: Student %d" + "scoring %.2f%n", (j + 1), getHighest(database[(double)i][(double)j], j)); */
			}
            }


	
		
		
	

				}	
			
			}

	

	