#include<bits/stdc++.h>
 
#define rep(i, a, b) for(int i=a; i<b; i++)
#define pb push_back
using namespace std;

vector<bool> visited(100);
vector<vector<int>> graph(100);

void DFS(int v) {
    visited[v] = true;
    for (int u : graph[v]) {
        if (!visited[u])
            DFS(u);
    }
}

bool solve(){
    int N, u, v, count=0;
    cin>>N;
    rep(i, 0, N){
        cin>>u>>v;
        graph[u].pb(v);
    }
    rep(i, 0, N){
        if(!visited[i]){
           DFS(i); 
           count++;
        }
    }
    if(count>1)
        return false;
    else 
        return true;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout<<solve();
    return 0;
} 
