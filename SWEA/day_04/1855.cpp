// LCA 알고리즘이 있다는 것을 모르고 처음에 선형으로 공통 조상을 찾았을 때에는 계속 시간초과가 발생했다.
// 그러다가 다른 방식으로 문제를 풀려고 하였지만 계속 풀리지 않았다.
// LCA 알고리즘에 대해 처음 배울 수 있었다.

#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cmath>

using namespace std;

class node {
public:
    int depth;
    vector<int> child;
};

// LCA를 찾는 알고리즘으로, 처음 배웠다.
inline int get_depth_of_lca(node *&nodes, int a, int b, vector<vector<int>> &parent, int max_k) {
    int tmp;
    // 노드 b가 더 아래에 있는 노드가 되도록 만들어 준다.
    if (nodes[a].depth > nodes[b].depth) {
        tmp = a;
        a = b;
        b = tmp;
    }

    // 노드 b를 노드 a의 높이까지 올려준다.
    // 이때 b와 a의 높이 차이가 예를들어 6이라면, 4만큼 올라가고, 2만큼 올라가면 된다.
    // 즉 2^2 만큼 올라간 뒤에 2^1 만큼 올라가면 된다.
    // 이는 6 = 110(2) 를 통해 알아낼 수 있다.
    for (int k = max_k; k >= 0; --k) {
        int power_k = 1 << k;
        if (nodes[b].depth - nodes[a].depth >= power_k) 
            b = parent[b][k];
    }

    // 노드 b를 노드 a의 높이까지 올려주었더니, 두 노드가 같다면 LCA는 노드 a가 된다.
    if (a == b)
        return nodes[a].depth;

    // 노드 a와 b의 높이를 맞춰주었다면, 이제 LCA 바로 밑의 노드까지 올린다.
    // 이때 LCA 까지 올리는 것이 아니라 LCA 바로 밑의 노드까지 올리는 이유는 노드 a와 노드 b의 2^k 번째 부모를 비교하기 때문이다.
    // 즉 2^k 번째 부모가 같지 않다면 2^k 번째까지 올리고, 같다면 그냥 냅둔다는 것이다.
    // 만약 LCA가 10번째 부모라면, 9번째 부모까지 올라가게 된다는 것이다.
    // 9 = 1001(2) 이므로 8번째 부모로 올라간뒤 1번째 부모로 올라가면 된다.
    for (int k = max_k; k >= 0; k--) {
        if (parent[a][k] == parent[b][k])
            continue;
        
        a = parent[a][k];
        b = parent[b][k];
    }

    // 노드 a는 LCA 바로 밑의 노드이므로 노드 a의 부모의 깊이를 반환한다. 
    return nodes[parent[a][0]].depth;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	cin >> T;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N;
        // parent[x][k] 는 노드 x의 2^k 번째 부모의 노드를 저장한다.
        vector<vector<int>> parent;
        int max_depth = 0;
        int max_k;
        long long count = 0;

        node *nodes;
        queue<int> q;
        bool *visited;  

        cin >> N;
        nodes = new node[N+1];

        visited = new bool[N+1];

        for (int i = 0; i <= N; ++i)
            visited[i] = false;

        parent.assign(N+1, vector<int>(18, 0));

        nodes[1].depth = 0;


        for (int i = 2; i <= N; ++i) {
            int p;
            cin >> p;
            parent[i][0] = p;
            
            nodes[i].depth = nodes[p].depth + 1;
            nodes[p].child.push_back(i);

            max_depth = max(max_depth, nodes[i].depth);
        }

        max_k = int(log2(max_depth)) + 1;


        // x의 2^k번째 부모는 x의 2^k-1 번째 부모의 2^k-1 번째 부모이다.
        for (int k = 1; k <= max_k; ++k) {
            for (int x = 1; x <= N; ++x) {
                parent[x][k] = parent[parent[x][k-1]][k-1];
            }
        }


        // bfs를 시작하기 전에 루트노드를 먼저 집어넣는다.
        q.push(1);
        visited[1] = true;
        int prev = -1;

        // bfs를 하면서 에지의 개수를 업데이트한다.
        // 이전에 방문한 노드에서 현재 노드에 방문할때 두 노드의 공통 조상까지 올라갔다가 내려 오기 때문에 LCA를 구해야 한다.
        while (!q.empty()) {
            int cur = q.front();
            q.pop();

            // 공통 조상 노드까지 올라갔다가 내려오는데 거치는 에지의 개수를 count에 더한다.
            if (prev != -1) {
                int upper_depth = get_depth_of_lca(nodes, prev, cur, parent, max_k);
                count += (nodes[prev].depth - upper_depth + nodes[cur].depth - upper_depth);
            }
            prev = cur;

            for (int i = 0; i < nodes[cur].child.size(); ++i) {
                int next = nodes[cur].child[i];

                if (!visited[next]) {
                    q.push(next);
                    visited[next] = true;

                }
            }
        }

        cout << '#' << test_case << ' ' << count << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}

