// 최대 에지 개수가 최대 노드 개수의 4배이므로 크러스컬 알고리즘을 사용한다.

#include<iostream>
#include<vector>
#include<tuple>
#include<algorithm>

using namespace std;

// 크러스컬 알고리즘에 사용되는 disjoint subset을 구현하는 inverted_tree의 노드
class node {
public:
    int parent;
    int depth;
};

// inverted_tree 초기화. 처음에는 모든 노드가 각자의 서로소 집합에 포함된다.
inline void init_set(node *&inverted_tree, int n) {
    for (int i = 1; i <= n; ++i) {
        inverted_tree[i].depth = 0;
        inverted_tree[i].parent = i;
    }
}

// 노드 j가 포함된 서로소 집합의 루트 노드를 반환한다.
inline int find_root(node *&inverted_tree, int i) {
    while (i != inverted_tree[i].parent)
        i = inverted_tree[i].parent;

    return i;
}

// 노드 i와 노드 j가 속한 서로소 집합을 합친다.
inline void merge_set(node *&inverted_tree, int i, int j) {
    int p1 = find_root(inverted_tree, i);
    int p2 = find_root(inverted_tree, j);
    
    if (inverted_tree[p1].depth == inverted_tree[p2].depth) {
        inverted_tree[p1].depth++;
        inverted_tree[p2].parent = p1;
    } else if (inverted_tree[p1].depth > inverted_tree[p2].depth) {
        inverted_tree[p2].parent = p1;
    } else {
        inverted_tree[p1].parent = p2;
    }
}


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
        // edges는 make_heap()을 통해 비용에 대한 min heap으로 만들 것이다.
        vector< tuple<int, int, int> > edges;
        int N, M;
        int count = 0;
        int min_cost = 0;
        node *inverted_tree;
        
        cin >> N;
        cin >> M;

        inverted_tree = new node[N+1];

        for (int i = 0; i < M; ++i) {
            int s, e, c;
            cin >> s >> e >> c;

            // min heap으로 만들기 위해 비용에 -를 붙여서 넣는다.
            edges.push_back({-c, s, e});
        }

        // min heap으로 만든다.
        make_heap(edges.begin(), edges.end());

        init_set(inverted_tree, N);

        // 비용이 낮은 순으로 edge를 하나씩 꺼내서 해당 에지를 선택할지 말지 결정한다.
        while (count < N-1) {
            pop_heap(edges.begin(), edges.end());
            tuple<int, int, int> t = edges.back();
            edges.pop_back();

            // 꺼낸 에지의 두 노드가 같은 서로소 집합에 포함되어 있다면, 해당 에지는 사이클을 생성한다.
            if (find_root(inverted_tree, get<1>(t)) == find_root(inverted_tree, get<2>(t)))
                continue;
            
            // 두 노드가 서로 다른 서로소 집합에 있다면 두 집합을 합치고, 해당 에지를 선택한다.
            merge_set(inverted_tree, get<1>(t), get<2>(t));
            count++;
            min_cost += -get<0>(t);
        }

        cout << '#' << test_case << ' ' << min_cost << endl;
    }
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}