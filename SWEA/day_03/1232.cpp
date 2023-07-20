#include<iostream>
#include<stack>

using namespace std;

class Node {
public:
    string item;
    Node* left;
    Node* right;

    Node(string new_item = "", Node* new_left = NULL, Node* new_right = NULL) {
        item = new_item;
        left = new_left;
        right = new_right;
    }
};


int operate(int arg1, int arg2, string op) {
    if (op == "-") return arg1 - arg2;
    if (op == "+") return arg1 + arg2;
    if (op == "*") return arg1 * arg2;
    
    return arg1 / arg2;
}

// postorder로 탐색하면서 연산을 수행한다.
Node *postorder(Node *root, stack<int> &stk) {
    if (root == NULL) return root;
    postorder(root->left, stk);
    postorder(root->right, stk);
    
    // 리프노드인 경우, 즉 숫자인 경우 스택에 push 한다.
    if (root->left == NULL) {
        stk.push(atoi((root->item).c_str()));
    } 
    // 리프노드가 아닌 경우, 즉 연산자인 경우 스택에서 숫자 두개를 빼서 연산한뒤 결과를 스택에 push한다.
    else {
        int arg2 = stk.top();
        stk.pop();
        int arg1 = stk.top();
        stk.pop();

        stk.push(operate(arg1, arg2, root->item));
    }
}

int main(int argc, char** argv)
{   
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);
	
    int test_case;
	int T;
	/*
	   아래의 freopen 함수는 input.txt 를 read only 형식으로 연 후,
	   앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
	   //여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
	   freopen 함수를 이용하면 이후 cin 을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
	   따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 함수를 사용하셔도 좋습니다.
	   freopen 함수를 사용하기 위해서는 #include <cstdio>, 혹은 #include <stdio.h> 가 필요합니다.
	   단, 채점을 위해 코드를 제출하실 때에는 반드시 freopen 함수를 지우거나 주석 처리 하셔야 합니다.
	*/
	//freopen("input.txt", "r", stdin);
	T = 10;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for(test_case = 1; test_case <= T; ++test_case)
	{   
        int N;
        int p, l, r;
        Node *root;
        string item;
        stack<int> stk;

        cin >> N;

        Node *nodes[10001];
        nodes[1] = new Node();
        root = nodes[1];

        // 노드 하나씩 입력받는다.
        for (int i = 1; i <= N; i++) {
            cin >> p >> item;

            if (atoi(item.c_str())) {
                nodes[p]->item = item;
            } else {
                cin >> l >> r;
                nodes[l] = new Node();
                nodes[r] = new Node();
                nodes[p]->item = item;
                nodes[p]->left = nodes[l];
                nodes[p]->right = nodes[r];
            }
        }

        postorder(root, stk);

        cout << '#' << test_case << ' ' << stk.top() << endl;
	}

	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}