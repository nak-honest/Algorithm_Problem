// 많이 헤맨 문제였다. K에 공통되는 부분들을 나눈다는 점을 생각하기 어려웠고, 횟수가 적은 순으로 힙에 넣는다는 점도 생각하기 어려웠다.

#include<iostream>
#include<queue>

using namespace std;

int main(int argc, char** argv)
{
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
        int A[10];

        // pq는 현재까지 누적 횟수가 작은 pair가 더 우선순위가 높다.
        priority_queue< pair<int, int> > pq;

        cin >> N;

        for (int i = 0; i < N; ++i)
            cin >> A[i];
        
        cin >> K;
        
        pq.push(make_pair(0, K));

        while (1) {
            int cur_cnt = -pq.top().first;
            int left = pq.top().second;
            pq.pop();

            if (left == 0) {
                cout << '#' << test_case << ' ' << cur_cnt  << endl;
                break;
            }

            for (int i = 0; i < N; ++i) {
                pq.push(make_pair(-(cur_cnt + left % A[i]), left / A[i]));
            }
            pq.push(make_pair(-(cur_cnt + left), 0));
        }

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
