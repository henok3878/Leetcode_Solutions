class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        Queue<Project> profitBased = new PriorityQueue<>(
            (a,b) ->(a.profit == b.profit) ? a.capital - b.capital  : b.profit - a.profit);
        
        Queue<Project> capitalBased = new PriorityQueue<>(
            (a,b) ->(a.capital == b.capital) ? b.profit - a.profit  : a.capital - b.capital);
        for(int p = 0; p < n ; p++){
            profitBased.add(new Project(profits[p],capital[p]));
        }
        
        while(k > 0 && !profitBased.isEmpty()){
            if(profitBased.peek().capital <= w){
                w += profitBased.poll().profit;
                k--;
            }
            else{
                capitalBased.add(profitBased.poll());
            }
            while(!capitalBased.isEmpty() && capitalBased.peek().capital <= w){
                profitBased.add(capitalBased.poll());
            }
            
        }
        
        return w;
        
        
    }
}

/*
    goal: increasing capital (maximazing total capital)
    
    constraint: resource is limited can only finish K projects 

    i/p: n projects wiht profit and capital needed to start it 
        
        out inital capital: w

*/

class Project{
    int profit;
    int capital;
    public Project(int profit, int capital){
        this.profit = profit;
        this.capital = capital;
    }
}