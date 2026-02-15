class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer>list=new ArrayList<>();
        Map<Integer,Integer>map=new HashMap<>();
        for(int i:nums){
            map.put(i,map.getOrDefault(i,0)+1);
        }
        for(Map.Entry<Integer,Integer>res:map.entrySet()){
            int val=res.getValue();
            if(val>1){
                list.add(res.getKey());
            }
        }
        return list;
    }
}