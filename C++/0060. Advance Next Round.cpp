// we have defined the necessary header files here for this problem.
// If additional header files are needed in your program, please import here.
#include<vector>
int main()
{  
  // please define the C++ input here. For example: int a,b; cin>>a>>b;;  
  // please finish the function body here.  
  // please define the C++ output here. For example:cout<<____<<endl; 
    int n,m;
    while(cin>>n>>m){
        int temp;
        int res = 0;
        for(int i=0;i<m;++i){
            cin>>temp;
            res += temp>0?1:0;
        }
        int num = temp;
        for(int i=m;i<n;++i){
            cin>>temp;
            if(temp==num && temp>0){
                res ++;
            }
        }
        cout<<res<<endl;
    }
    return 0;
}
