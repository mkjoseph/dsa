public int nthSuperUglyNumber(int n, int[] primes) {
    int[] ugly = new int[n];
    int[] indexes = new int[primes.length];
    int[] values = new int[primes.length];
    ugly[0] = 1;

    for (int i = 1; i < n; i++) {
        int min = Integer.MAX_VALUE;
        for (int j = 0; j < primes.length; j++) {
            values[j] = ugly[indexes[j]] * primes[j];
            min = Math.min(min, values[j]);
        }

        ugly[i] = min;

        for (int j = 0; j < primes.length; j++) {
            if (values[j] == min) {
                indexes[j]++;
            }
        }
    }

    return ugly[n - 1];
}


// Pass 2

public int nthSuperUglyNumberHeap(int n, int[] primes) {
    int[] ugly = new int[n];

    PriorityQueue<Num> pq = new PriorityQueue<>();
    for (int i = 0; i < primes.length; i++) pq.add(new Num(primes[i], 1, primes[i]));
    ugly[0] = 1;

    for (int i = 1; i < n; i++) {
        ugly[i] = pq.peek().val;
        while (pq.peek().val == ugly[i]) {
            Num nxt = pq.poll();
            pq.add(new Num(nxt.p * ugly[nxt.idx], nxt.idx + 1, nxt.p));
        }
    }

    return ugly[n - 1];
}

/**
 * Represents a number with its value, index, and priority.
 */
private class Num implements Comparable<Num> {
    int val;
    int idx;
    int p;

    /**
     * Constructs a Num object with the specified value, index, and priority.
     * 
     * @param val The value of the number.
     * @param idx The index of the number.
     * @param p   The priority of the number.
     */
    public Num(int val, int idx, int p) {
        this.val = val;
        this.idx = idx;
        this.p = p;
    }

    @Override
    public int compareTo(Num that) {
        return this.val - that.val;
    }
}