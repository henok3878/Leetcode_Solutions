class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        
        for(int i = 0; i < flowerbed.length;i++){
            int left = (i - 1 < 0) ? 0 : flowerbed[i - 1];
            int right = (i + 1 >= flowerbed.length) ? 0 : flowerbed[i + 1] ;
            if(flowerbed[i] == 0 && left == 0 && right == 0){
                n--;
                flowerbed[i] = 1;
            }  
        }
        return n <= 0;
    }
}
/*
st: 3:9

test: 3:12

sub: 3:16 

*/