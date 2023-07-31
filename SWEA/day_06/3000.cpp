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
        int N, A;
        int X, Y;
        long long answer = 0;

        // 매번 중간 값을 저장
        int mid;

        // mid 보다 작은 값들을 넣는 max heap
        priority_queue<int> smaller;

        // mid 보다 큰 값들을 넣는 min heap
        priority_queue<int> larger;

        cin >> N >> A;

        mid = A;

        for (int i = 0; i < N; ++i) {
            cin >> X >> Y;
            
            // X와 Y 사이에 min이 존재한다면 min은 유지된다. X와 Y는 각자 알맞는 heap에 넣는다.
            if (min(X, Y) <= mid && max(X, Y) >= mid) {
                smaller.push(min(X, Y));
                larger.push(-max(X, Y));
            } 
            // X와 Y 둘다 min보다 크다면 min은 min 다음의 값으로 바뀐다.
            // min 다음의 값은 larger에 X와 Y를 넣은 후, 그중에서 가장 작은 값이다.
            // 따라서 min은 smaller에 집어넣고, X와 Y를 larger에 넣은 후 가장 작은 값을 mid로 삼는다.
            else if (min(X, Y) > mid) {
                smaller.push(mid);
                larger.push(-X);
                larger.push(-Y);
                mid = -larger.top();
                larger.pop();
            } 
            // X와 Y 둘다 min보다 작다면 min은 min 이전의 값으로 바뀐다.
            // min 이전의 값은 smaller에 X와 Y를 넣은 후, 그중에서 가장 큰 값이다.
            // 따라서 min은 larger에 집어넣고, X와 Y를 smaller에 넣은 후 가장 큰 값을 mid로 삼는다.
            else {
                larger.push(-mid);
                smaller.push(X);
                smaller.push(Y);
                mid = smaller.top();
                smaller.pop();
            }

            // answer 업데이트
            answer += mid;
            answer %= 20171109;
        }

        cout << '#' << test_case << ' ' << answer << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}

