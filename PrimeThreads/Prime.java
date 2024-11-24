/*Name: Emmanuel Nnadi
 * Date: 11/06/2024
 * Class: CPSC 245
 * Assignment: PrimeThreads
 * Description: A program that computes the sum of all primes within a range of numbers using multiple threads.
 * Exit status:
 * 0 on success
 * 1 Too few command line args (0).
 * 2 Expected an even number of agrs
 * 3 Must be an integer
 * 4 Thread Interrupted
 * 5 start must be less than end and both must be positive
 * 6 Worker is null or NullPointerExpection
 */

import java.util.ArrayList;
import java.util.Properties;

class Prime {

	public static void main(String[] args) {
		id();
		// check command line arguments
		if (args.length == 0) {
			System.err.println("*** ERROR: Too few command line args (0)");
			System.exit(1);
		}
		if (args.length % 2 != 0) {
			System.err.println("*** ERROR: Expected an even number of args");
			System.exit(2);
		}
		// create threads
		int threads_count = args.length / 2;
		System.out.printf("Creating %d thread(s)\n", threads_count);

		ArrayList<Thread> threads = new ArrayList<>();
		ArrayList<Worker> workers = new ArrayList<>();

		try {
			for (int i = 0; i < threads_count; i++) {
				int start = Integer.parseInt(args[2 * i]);
				int end = Integer.parseInt(args[2 * i + 1]);

				// check arguments
				if (start < 0 || end < 0 || start >= end) {
					System.err.println("*** ERROR: start must be less than end and both must be positive");
					System.exit(4);
				}
				Worker worker = new Worker(start, end);
				workers.add(worker);// add worker
				Thread t = new Thread(worker);
				t.start();// start thread
				threads.add(t);// add thread
			}

			// join threads
			for (int i = 0; i < threads_count; i++) {
				threads.get(i).join();
			}

			// get results
			double grand_sum = 0;
			for (int i = 0; i < threads_count; i++) {
				if (workers.get(i) == null) {// check if worker is null
					System.err.println("*** ERROR: Worker is null");
					System.exit(6);
				}

				grand_sum += workers.get(i).getResult();
				System.out.printf("Sum of all primes [%,8d - %,9d) is %,13.0f\n", workers.get(i).getStart(),
						workers.get(i).getEnd(), workers.get(i).getResult());
			}
			// print grand sum
			System.out.printf("\nThe grand sum of all primes calculations is %,13.0f\n", grand_sum);

		} catch (NumberFormatException e) {
			System.err.println("*** ERROR: Must be an integer");
			System.exit(3);
		} catch (InterruptedException e) {
			System.err.println("*** ERROR: Thread Interrupted");
			System.exit(5);
		} catch (NullPointerException e) {
			System.err.println("*** ERROR: null at line: " + e.getStackTrace()[0].getLineNumber());
			System.exit(6);
		}
		id();
	}

	// -----------------------------------------------
	// print id and system info
	// -----------------------------------------------
	private static void id() {
		final String YOUR_NAME = "Emmanuel Nnadi";

		int cores = Runtime.getRuntime().availableProcessors();
		String osName = System.getProperty("os.name");
		String osVer = System.getProperty("os.version");
		String osArch = System.getProperty("os.arch");
		String javaVer = System.getProperty("java.version");
		String javaName = System.getProperty("java.vm.name");

		System.out.printf("\n%14s | %s (%s) | Cores: %d\n", osArch, osName, osVer, cores);
		System.out.printf("%14s | %s\n", javaVer, javaName);
		System.out.printf("%14s | %s\n\n", "PrimeThreads", YOUR_NAME);
	}
}

class Worker implements Runnable {

	private final int start;
	private final int end;
	private double result;
	private long threadId;

	Worker(int start, int end) {
		this.start = start;
		this.end = end;
		this.result = 0;
	}

	public double getResult() {
		return result;
	}

	public int getStart() {
		return start;
	}

	public int getEnd() {
		return end;
	}

	@Override
	public void run() {
		threadId = Thread.currentThread().threadId();
		System.out.printf("Thread [%03d] created\n", threadId);
		result = computeTotal(start, end);
	}

	// -----------------------------------------------------------
	// sum up primes within range [start, finish)
	// -----------------------------------------------------------
	private static double computeTotal(int start, int finish) {
		double total = 0;

		for (int i = start; i < finish; i++) {
			if (Slow_isPrime(i)) {
				total += i;
			}
		}

		return total;
	}

	// ------------------------------------------------
	// determines if a number is a prime number
	// you must use this code, and can't modify it.
	// -----------------------------------------------
	private static boolean Slow_isPrime(int val) {
		int i = 0;

		if (val <= 1) {
			return false;
		}

		if (val == 2) {
			return true;
		}

		if ((val % 2) == 0) {
			return false;
		}

		for (i = 3; i < val; i++) {
			if ((val % i) == 0) {
				return false;
			}
		}

		return true;
	}
}
