// we have defined the necessary header files here for this problem.
// If additional header files are needed in your program, please import here.
#include<vector>
#include<cmath>
int main()
{  
  // please define the C++ input here. For example: int a,b; cin>>a>>b;;  
  // please finish the function body here.  
  // please define the C++ output here. For example:cout<<____<<endl; 
    int n;
    while(cin>>n){
        string res(n+1,0);
        string temp(1,1);
        
        for(int i=1;i<=n;++i){
            int m = temp.size();
            for(int j=m-1;j>=0;j--){
                res[j+n+1-m] += temp[j]*3;
                res[j-1+n+1-m] += res[j+n+1-m]/10;
                res[j+n+1-m] = res[j+n+1-m]%10;
            }
            temp = res;
            res = string(n+1,0);          
        }
        res = temp;
        int flag = 1;
        for(int i=res.size()-1;i>=0;--i){
            res[i] += flag;
            flag = res[i]/10;
            res[i] %= 10;
            if(flag==0) break;
        }
        flag = 0;
        for(int i=0;i<res.size();++i){
            res[i] += 10*flag;
            flag = res[i]%2;
            res[i] /= 2;
        }
        
        for(auto&c:res) c+='0';
        int i;
        for(i=0;i<res.size();++i){
            if(res[i]!='0'){
                break;
            }
        }
        cout<<res.substr(i)<<endl;
    }
    return 0;
}
