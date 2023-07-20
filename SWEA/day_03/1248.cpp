#include<iostream>

using namespace std;

class Node {
public:
    int item;
    Node* left;
    Node* right;
    Node* parent;
    int depth;

    Node(int new_item = -1, Node* new_left = NULL, Node* new_right = NULL, Node* new_parent = NULL, int new_depth = -1) {
        item = new_item;
        left = new_left;
        right = new_right;
        parent = new_parent;
        depth = new_depth;
    }
};

// 트리를 순회하며 depth를 업데이트 한다.
void update_depth(Node* root, int depth) {
    if (root == NULL) return;

    root->depth = depth;
    update_depth(root->left, depth+1);
    update_depth(root->right, depth+1);
}

// 공통 조상 정보를 얻는다.
int get_ancestor(Node *nodes, int c1, int c2) {
    Node* p1 = nodes[c1].parent;
    Node* p2 = nodes[c2].parent;

    while (p1->depth > p2->depth) {
        p1 = p1->parent;
    }
    while (p1->depth < p2->depth) {
        p2 = p2->parent;
    }

    while (p1 != p2) {
        p1 = p1->parent;
        p2 = p2->parent;
    }

    return p1->item;
}

// root 노드를 루트로 하는 서브트리의 크기를 구한다.
void inorder(Node* root, int* count) {
    if (root == NULL) return;
    inorder(root->left, count);
    inorder(root->right, count);

    *count += 1;
}

int main(int argc, char** argv)
{   
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);
	
    int test_case;
	int T;

	cin >> T;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for(test_case = 1; test_case <= T; ++test_case)
	{   
        int V, E, c1, c2;
        int p, c;
        Node root;
        int count = 0;

        cin >> V >> E >> c1 >> c2;

        Node *nodes = new Node[V+1];

        for(int i = 1; i <= V; i++) {
            nodes[i].item = i;
        }

        // 에지를 하나씩 입력받는다.
        for (int i = 0; i < E; i++) {
            cin >> p >> c;
            nodes[c].parent = &nodes[p];

            if (nodes[p].left == NULL) {
                nodes[p].left = &nodes[c];
            } else {
                nodes[p].right = &nodes[c];
            }
        }

        root = nodes[1];

        update_depth(&root, 0);

        int ancestor = get_ancestor(nodes, c1, c2);
        inorder(&nodes[ancestor], &count);

        cout << '#' << test_case << ' ' << ancestor << ' ' << count << endl;
	}

	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}