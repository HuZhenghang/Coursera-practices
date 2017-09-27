#include<iostream>
#include<vector>
#include<cstring> 
using namespace std;

struct edge{
    int v,t;
    edge(int v1,int t1): v(v1),t(t1) {}
};

struct plan{
	int v,id;
	plan(int v1,int id): v(v1),id(id) {}
};

vector<edge> a[300005];//邻接表 
vector<plan> plans[300005];//记录询问 
int lca[300005];//最近公共祖先 
int prev1[300005];//时间戳 
int time=0;//时间 
int bcj[300005];//并查集 
int visit[300005];
int findroot(int x){
	if(bcj[x]==x) return x;
	return findroot(bcj[x]);
}
int n,m;
void dfs1(int p){//求lca 
	time++;
	prev1[p]=time;
	bcj[p]=p;
	visit[p]=1;
	for(int i=0;i<a[p].size();i++){
		int v=a[p][i].v;
		if(visit[v]==0){
			dfs1(v);
			bcj[v]=p;
		}	
	}
	
	for(int i=0;i<plans[p].size();i++){
		int v=plans[p][i].v;
		int id=plans[p][i].id;
		if( prev1[v] !=0 ) lca[id]=findroot(v);		
	}

}
int dist[300005];
void dfs2(int p,int d){//求dist 
    dist[p]=d;
    visit[p]=1;
	for(int i=0;i<a[p].size();i++){
		int v=a[p][i].v;
		if(visit[v]==0) dfs2(v,d+a[p][i].t);		
	}
	
}
int ti[300005];

int main(){

    cin>>n>>m;
    for(int i=1;i<=n-1;i++){
        int u1,v1,t1;
        cin>>u1>>v1>>t1;
        a[u1].push_back( edge(v1,t1) );
        a[v1].push_back( edge(u1,t1) );
    }
    
    for(int i=1;i<=m;i++){
        int start,end;
        cin>>start>>end;
        plans[start].push_back( plan(end,i) );
        plans[end].push_back( plan(start,i) );
    }
    
    dfs1(1);
	memset(visit,0,sizeof(visit));
	


int min=1000000000;	
	for(int i=1;i<=n;i++){
		for(int j=0;j<a[i].size();i++){
			int max=0,dis=a[i][j].t,v1=a[i][j].v;
			int l;
			for(l=0;l<a[v1].size();l++) if(a[v1][l].v==i) 
			a[v1][l].t=0;
			a[i][j].t=0;
			l--;
		
			dfs2(1,0);
			
			for(int k=1;k<=n;k++){//便利所有运输方案 
				for(int y=0;y<plans[k].size();y++){
					int id=plans[k][y].id;
					if(ti[id]==0) ti[id]=dist[k]+dist[plans[k][y].v]-2*dist[lca[id]];
				}
			}

			for(int o=1;o<=m;o++) if( ti[o]>max ) max=ti[o];//该计划里的最大值 

			if(max<min) min=max;
			a[i][j].t=dis;
			a[v1][l].t=dis;
			memset(visit,0,sizeof(visit));
			memset(ti,0,sizeof(ti));
		}
	}
  cout<<min<<endl; 
    
    return 0;
}
