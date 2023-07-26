// 이전에 LCS 문제를 풀어서 금방 풀었다.

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
        string s1, s2;
        int len1, len2;
        int **dp;

        cin >> s1 >> s2;
        len1 = s1.size();
        len2 = s2.size();

        dp = new int*[len1+1];
        for (int i = 0; i <= len1; ++i)
            dp[i] = new int[len2+1];

        for (int i = 0; i <= len1; ++i)
            dp[i][0] = 0;
        for (int j = 0; j <= len2; ++j)
            dp[0][j] = 0;


        for (int i = 1; i <= len1; ++i) {
            for (int j = 1; j <= len2; ++j) {
                if (s1.at(i-1) != s2.at(j-1)) {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                } else {
                    dp[i][j] = dp[i-1][j-1] + 1;
                }
            }
        }

        cout << '#' << test_case << ' ' << dp[len1][len2] << endl;

        for (int i = 0; i <= len1; ++i)
            delete[] dp[i];
        delete[] dp;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
