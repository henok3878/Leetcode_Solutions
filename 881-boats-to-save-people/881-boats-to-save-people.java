class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int i = 0, j = people.length - 1, count = 0;
        while(i <= j){
            if(people[j] + people[i] <= limit){i++; j--;}
            else j--;
            count++;
        }
        return count;
    }
}
