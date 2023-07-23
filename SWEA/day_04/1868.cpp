#include<iostream>
#include<vector>
#include<queue>

using namespace std;

// 인접한 상하좌우, 대각선 8칸
int adjacent[8][2] = {
    {-1, -1},
    {-1, 0},
    {-1, 1},
    {0, -1},
    {0, 1},
    {1, -1},
    {1, 0},
    {1, 1}
};

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin>>T;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N;
        vector<vector<char>> board;
        vector<vector<bool>> check;
        int count = 0;

        cin >> N;
        board.assign(N, vector<char>(N, 0));
        check.assign(N, vector<bool>(N, false));

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cin >> board[i][j];
                if (board[i][j] == '.') {
                    // . 인 경우 먼저 0으로 바꿔준다.
                    board[i][j] = 0;
                }
                else {
                    // * 은 체크할수 없기 때문에 true로 설정해준다.
                    check[i][j] = true;
                }
            }
        }

        // 각 * 주변으로 숫자를 업데이트 해준다.
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (board[i][j] == '*') {
                    for (int k = 0; k < 8; ++k) {
                        int x = i + adjacent[k][0];
                        int y = j + adjacent[k][1];

                        // 각 * 주변이 범위 내에 존재하고, *이 아닌 경우에만 업데이트 해준다.
                        if (x >= 0 && x < N && y >= 0 && y < N && board[x][y] != '*')
                            ++board[x][y];
                    }
                }
            }
        }

        // 전체 칸을 확인하면서 0을 찾는다.
        // 0이라면 bfs를 통해 주변을 연쇄적으로 check 해준다.
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                // 아직 체크하지 않은 0이라면 bfs를 하면서 주변을 모두 check하고, 주변의 0에 대해서도 연쇄적으로 반복한다.
                if (!check[i][j] && board[i][j] == 0) {
                    // 0을 발견할때마다 연쇄적으로 check하기 때문에 count를 1씩 증가시킨다.
                    ++count;
                    queue<pair<int, int>> q;
                    
                    // 현재 발견한 0의 인덱스를 큐에 넣고 bfs를 시작한다.
                    q.push({i, j});
                    check[i][j] = true;

                    while (q.size() > 0) {
                        int x = q.front().first;
                        int y = q.front().second;
                        q.pop();

                        // 큐에는 주변의 0만 집어넣는다. 따라서 큐 주변의 숫자들을 모두 check하고, 큐 그중 아직 check하지 않은 0이 있다면 큐에 넣어준다.
                        for (int k=0; k < 8; ++k) {
                            int adj_x = x + adjacent[k][0];
                            int adj_y = y + adjacent[k][1];

                            // 주변 칸 중 유효하고, 아직 체크하지 않은 경우 먼저 체크해준다.
                            if (adj_x >= 0 && adj_x < N && adj_y >= 0 && adj_y < N && !check[adj_x][adj_y]) {
                                check[adj_x][adj_y] = true;
                                // 그중 0인 칸은 큐에 넣는다.
                                if (board[adj_x][adj_y] == 0)
                                    q.push({adj_x, adj_y});
                            }
                        }
                    }
                }
            }
        }

        // 0을 통해 연쇄적으로 밝히는 경우를 제외하고는 모두 한칸당 한번씩 check해 주어야 한다.
        // 따라서 아직 check하지 않은 칸의 수를 모두 더한다.
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (!check[i][j])
                    ++count;
            }
        }

        cout << '#' << test_case << ' ' << count << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}