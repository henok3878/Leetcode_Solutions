class Solution {
	public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        
        List<List<Node>> graph = new ArrayList<>();
        for(int city = 0; city < n ; city++) graph.add(new ArrayList<>());
        
        for(int[] flight : flights){
            int u = flight[0], v = flight[1], price = flight[2];
            graph.get(u).add(new Node(v,price));
        }

		Queue<Node> q = new LinkedList<Node>();
		q.add(new Node(src, 0));
		int[] minDist = new int[n];
		Arrays.fill(minDist, Integer.MAX_VALUE);
		int count = -1;

        while(!q.isEmpty()) {
			if(count == k) {
				break;
			}
			for(int i = q.size() - 1; i >= 0; --i) {
				Node curr = q.poll();
				int node = curr.city;
				int weight = curr.price;
                for(Node adj : graph.get(node)){
                    int city = adj.city;
                    int w = weight + adj.price;
                    if (w < minDist[city]) {
                        minDist[city] = w;
                        if(city == dst) continue;
                        q.add(new Node(city, w));
                    }
                }
			}
			count++;
		}
		return minDist[dst] != Integer.MAX_VALUE ? minDist[dst] : -1;
	}
}
class Node{
    int city;
    int price;
    Node(int city, int price){
        this.city = city;
        this.price = price;
    }
    public String toString(){
        return "(" + city + ":" + price + ")";
    }
}
