// Calvin Gagliano 
// @calgagi
// Oregon State University
// Competitive Programming Template
#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using ull = unsigned long long;
using ii = pair<int, int>;

int main() {
    ios_base::sync_with_stdio(false);  
    cin.tie(NULL);
    srand(chrono::steady_clock::now().time_since_epoch().count()); 
    // freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout); 
    
    ll n;
    cin >> n;
    stack<ll> s;
    s.push(1LL);
    ll ans = 0;
    while (!s.empty()) {
        ll x = s.top();
        s.pop();
        if (x > n) {
            continue;
        }
        ans++;
        s.push(x*10);
        s.push(x*10+1);
    }
    cout << ans << endl;


    return 0;
}
