// we have defined the necessary header files here for this problem.
// If additional header files are needed in your program, please import here.
#include <vector>
int main()
{  
  // please define the C++ input here. For example: int a,b; cin>>a>>b;;  
  // please finish the function body here.  
  // please define the C++ output here. For example:cout<<____<<endl; 

    int n,m;
    while(cin>>n>>m){
        vector<vector<int>> arr(n,vector<int>(m,0));
        int temp;
        int cnt=0;

        while(cin>>temp){
            arr[cnt/m][cnt%m] = temp;
            cnt++;
        }
        
        for(int i=1;i<n;++i){
            arr[i][0] += arr[i-1][0];
        }
        
        for(int j=1;j<m;++j){
            arr[0][j] += arr[0][j-1];
        }
        
        for(int i=1;i<n;++i){
            for(int j=1;j<m;++j){
                arr[i][j] += max(arr[i-1][j],arr[i][j-1]);
            }
        }
        
        cout<<arr[n-1][m-1]<<endl;
    }
    return 0;
}
