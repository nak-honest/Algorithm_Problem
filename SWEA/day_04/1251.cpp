#include<iostream>
#include<climits>
#include<cmath>

using namespace std;

long long get_distance(long long a[2], long long b[2]) {
    return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]);
}

int main(int argc, char** argv)
{
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);
    
	int test_case;
	int T;

    // freopen("input.txt", "r", stdin);

	cin>>T;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N;
        double E;
        long long L = 0;
        long long xy[1001][2];
        long long distance[1001];

        cin >> N;
        
        for (int i = 0; i < N; ++i)
            cin >> xy[i][0];

        for (int i = 0; i < N; ++i)
            cin >> xy[i][1];


        // Prim's algorithm을 통해 MST를 찾으면서 L을 업데이트한다.
        
        for (int i = 0; i < N; ++i) {
            distance[i] = get_distance(xy[0], xy[i]);
        }

        for (int iteration = 0; iteration < N-1; ++iteration) {
            int next;
            long long min_edge = LLONG_MAX;

            for (int i = 0; i < N; ++i) {
                if (distance[i] != 0 && min_edge > distance[i]) {
                    min_edge = distance[i];
                    next = i;
                }
            }

            distance[next] = 0;
            L += min_edge;

            for (int i = 0; i <= N; ++i) {
                if (distance[i] != 0 && distance[i] > get_distance(xy[i], xy[next]))
                    distance[i] = get_distance(xy[i], xy[next]);
            }
        }
        
        cin >> E;

        cout << '#' << test_case << ' ' << (long long)round(L*E) << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}