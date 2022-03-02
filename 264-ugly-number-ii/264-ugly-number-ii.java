class Solution {
    public int nthUglyNumber(int n) {
		if(n<=0) return 0;
		int twosPointer=0,threesPointer=0,fivesPointer=0;
		List<Integer> uglies = new ArrayList<Integer>();
		uglies.add(1);
		while(uglies.size() < n)
		{
			int nextUgly = Math.min(uglies.get(twosPointer)*2,Math.min(uglies.get(threesPointer)*3,uglies.get(fivesPointer)*5));
			uglies.add(nextUgly);
			if(uglies.get(twosPointer)*2==nextUgly) twosPointer++;
			if(uglies.get(threesPointer)*3==nextUgly) threesPointer++;
			if(uglies.get(fivesPointer)*5==nextUgly) fivesPointer++;
		}
		return uglies.get(uglies.size()-1);
	}
}