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
        Map<Integer,Employee> idToEmp= new HashMap<>();
        for(Employee emp : employees) idToEmp.put(emp.id, emp);
        
        return dfs(id,idToEmp);
    }
    
    
    private int dfs(int id, Map<Integer,Employee> map){
        Employee emp = map.get(id);
        int imp = emp.importance;
        for(int i : emp.subordinates){
            imp += dfs(i,map);
        }
        return imp;
        
    }
}