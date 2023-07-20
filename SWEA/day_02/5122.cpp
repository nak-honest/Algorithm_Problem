#include<iostream>
#include<list>

using namespace std;

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
        int N, M, L;
        char command;
        int item, arg1, arg2;
        list<int> seq;
        list<int>::iterator it;
        int answer;

        cin >> N >> M >> L;

        for (int i = 0; i < N; i++) {
            cin >> item;
            seq.push_back(item);
        }

        for (int i = 0; i < M; i++) {
            cin >> command;
            if (command == 'I') {
                cin >> arg1 >> arg2;

                it = seq.begin();
                for (int j = 0; j < arg1; j++) {
                    it++;
                }

                seq.insert(it, arg2);
            } else if (command == 'D') {
                cin >> arg1;
                
                it = seq.begin();
                for (int j = 0; j < arg1; j++) {
                    it++;
                }

                seq.erase(it);
            } else if (command == 'C') {
                cin >> arg1 >> arg2;

                it = seq.begin();
                for(int j = 0; j < arg1; j++) {
                    it++;
                }

                it = seq.erase(it);
                seq.insert(it, arg2);
            }
        }

        if (L >= seq.size()) {
            answer = -1;
        } else {
            it = seq.begin();
            for (int i = 0; i < L; i++) {
                it++;
            }
            answer = *it;
        }

        cout << '#' << test_case << ' ' << answer << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}