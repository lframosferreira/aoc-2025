// pescoço pra baixo é canela

#include <vector>
#include <string>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <list>
#include <iostream>

using namespace std;

#define _                                                                      \
  ios_base::sync_with_stdio(0);                                                \
  cin.tie(0);
#define endl '\n'
#define sz(v) (int)v.size()
#define f first
#define s second
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define umap unordered_map
#define uset unordered_set
#define all(v) begin(v), end(v)
#define rall(v) rbegin(v), rend(v)

#define dbg(x) cout << #x << " = " << x << endl

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef tuple<int, int, int> iii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<double> vd;
typedef vector<vd> vvd;

const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fll;


vector<string> mapa;
int n,m;

int oob(int i, int j) {
    return i < 0 or j < 0 or i >= n or j >= m;
}

vector<ii> mvs = {{-1,-1}, {1,1},{0,-1},{-1,0},{1,0},{0,1}, {1,-1}, {-1, 1}};

int ok(int i, int j)
{
   int cnt=0;
   if (mapa[i][j]!='@') return 0;
  for (auto [di,dj]:mvs)if (oob(i+di,j+dj)) {continue;} else cnt+=mapa[i+di][j+dj]=='@'; 

      return cnt <4;
}

int main() {
  _
        string line;
        while (cin>>line){
            mapa.pb(line);
        }
        int ans=0;
        n=sz(mapa);
        m = sz(mapa[0]);
        for (int i = 0; i < n;i++) for (int j = 0; j < m; j++) ans+=ok(i,j);
        cout << ans << endl;
      exit(0);
}
