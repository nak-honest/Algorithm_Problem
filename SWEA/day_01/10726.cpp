#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
    int test_case;
    int T;
    string answer[2] = {"OFF", "ON"};

    cin>>T;
    /*
       여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    */
    for(test_case = 1; test_case <= T; ++test_case)
    {
        int N, M;
        bool is_on = true;

        cin >> N >> M;

        for (int i = 0; i < N; i++) {
            // M의 i비트가 1이 아니라면 for문 탈출
            if (!(M & (1 << i))) {
                is_on = false;
                break;
            }
        }

        cout << '#' << test_case << ' ' << answer[(int)is_on] << endl;
    }
    return 0;//정상종료시 반드시 0을 리턴해야합니다.
}