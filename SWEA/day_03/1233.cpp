#include<iostream>

using namespace std;

bool is_valid(char tree[], int last_parent_index, int n) {
    // 자식노드가 있다면(즉 부모노드라면) 해당 노드에는 숫자가 아닌 연산자가 들어 있어야 한다.
    for (int i = 1; i <= last_parent_index; i++) {
        if (isdigit(tree[i])) return false;
    }

    // 자식노드가 없다면(즉 리프노드라면) 해당 노드에는 숫자가 들어 있어야 한다.
    for (int i = last_parent_index + 1; i <= n; i++) {
        if (!isdigit(tree[i])) return false;
    }

    return true;
}

int main(int argc, char** argv)
{   
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);
	
    int test_case;
	int T;
	
	T = 10;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for(test_case = 1; test_case <= T; ++test_case)
	{   
        int N;
        char tree[201];
        char item;
        int dump;
        int last_parent_index;
        bool answer = true;

        tree[0] = 0;

        cin >> N;

        // 노드 하나씩 입력받는다.
        for (int i = 1; i <= N; i++) {
            cin >> dump >> item;

            // 왼쪽 자식이 있다면 왼쪽 자식 노드 번호를 입력받는다.
            if ((i<<1) <= N) {
                cin >> dump;
            }
            // 오른쪽 자식이 있다면 오른쪽 자식 노드 번호를 입력받는다.
            if ((i<<1) + 1 <= N) {
                cin >> dump;
            }

            tree[i] = item;
        }

        // 마지막 부모노드의 인덱스를 찾는다.
        last_parent_index = 1;
        while ((last_parent_index << 1) <= N) {
            last_parent_index <<= 1;
        }

        last_parent_index >>= 1;

        while (((last_parent_index + 1) << 1) <= N) {
            ++last_parent_index;
        }

        answer = is_valid(tree, last_parent_index, N);

        cout << '#' << test_case << ' ' << answer << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}