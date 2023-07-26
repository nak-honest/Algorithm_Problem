// 유명한 냅색 문제이다.

#include<iostream>

using namespace std;

int main(int argc, char** argv)
{   
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);

	int test_case;
	int T;

	//freopen("input.txt", "r", stdin);
	cin>>T;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N, K;
        int *V, *C;
        int **dp;

        cin >> N >> K;

        V = new int[N+1];
        C = new int[N+1];
        dp = new int*[N+1];

        for (int i = 0; i <= N; ++i)
            dp[i] = new int[K+1];
        
        for (int i = 1; i <= N; ++i)
            cin >> V[i] >> C[i];


        for (int i = 0; i <= N; ++i)
            dp[i][0] = 0;
        for (int v = 0; v <= K; ++v)
            dp[0][v] = 0;


        for (int i = 1; i <= N; ++i) {
            for (int v = 1; v <= K; ++v) {
                if (V[i] > v) {
                    dp[i][v] = dp[i-1][v];
                } else {
                    dp[i][v] = max(dp[i-1][v], dp[i-1][v-V[i]] + C[i]);
                }
            }
        }

        cout << '#' << test_case << ' ' << dp[N][K] << endl; 
        
        delete[] V;
        delete[] C;
        for (int i = 0; i <= N; ++i)
            delete[] dp[i];
        delete[] dp;
    }
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
