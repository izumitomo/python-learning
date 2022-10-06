#include <stdio.h>
#include
int main(void){
    int n,st[1000],en[1000],max[1000],min[1000],tr_max = 0,tr_min = 10000000;
    char str[1000];
    fgets(str, sizeof(str), stdin);
    sscanf(str,"%d\n",&n);
    for(int i = 0 ; i < n ; i++){
        fgets(str, sizeof(str), stdin);
        sscanf(str,"%d %d %d %d\n",&st[i], &en[i], &max[i], &min[i]);
    }
    for(int i = 0 ; i < n ; i++){
        if(tr_max < max[i]){
            tr_max = max[i];
        }
        if(tr_min > min[i]){
            tr_min = min[i];
        }
    }
    printf("%d %d %d %d\n", st[0],en[n-1],tr_max,tr_min);
    return 0;
}
