#include<iostream>
#include<queue>

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
        priority_queue<int> max_heap;

        int N, command, x;

        cin >> N;

        cout << '#' << test_case;

        for (int i = 0; i < N; ++i) {
            cin >> command;
            if (command == 1) {
                cin >> x;
                max_heap.push(x);
            } else if (max_heap.size() == 0) {
                cout << ' ' << -1;
            } else {
                cout << ' ' << max_heap.top();
                max_heap.pop();
            }
        }

        cout << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}