int equalSubstring(char* s, char* t, int maxCost) {
    int N = strlen(s);  //先知道字串的長度
    int ans = 0, j = 0;
    for(int i=0; i<N; i++){ // 字串的迴圈
        maxCost -= abs( s[i] - t[i] ); //c語言直接減i頭
        while(maxCost<0){
            maxCost += abs( s[j] - t[j] ); //小心, 是j尾巴
            j += 1;
        }
        if(i-j+1>ans) ans = i-j+1; //更新答案
    }
    return ans; 
}