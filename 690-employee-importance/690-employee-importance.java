/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    public int getImportance(List<Employee> employees, int id) {
        Set<Integer> visited = new HashSet<>();
        Map<Integer,Employee> idToEmp= new HashMap<>();
        for(Employee emp : employees) idToEmp.put(emp.id, emp);
        
        return dfs(id,idToEmp,visited);
    }
    
    
    private int dfs(int id, Map<Integer,Employee> map, Set<Integer> visited){
        if(visited.contains(id)) return 0;
        Employee emp = map.get(id);
        int imp = emp.importance;
        visited.add(id);
        for(int i : emp.subordinates){
            imp += dfs(i,map,visited);
        }
        return imp;
        
    }
}