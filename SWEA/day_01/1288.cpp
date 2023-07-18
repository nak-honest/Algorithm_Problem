#include <iostream>

#define ALL_NUM 1023 // 1023 = 0b1111111111

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
        int N;
        // 숫자 i를 보았다면 num_bit의 i번째 비트는 1이 된다. 
        int num_bit = 0;
        int k = 1;

        cin >> N;
        
        while (1) {
            int num = N * k;
            // num의 각 자리의 숫자를 num_bit에 추가한다.
            while (num > 0) {
                num_bit |= (1 << (num % 10));
                num /= 10;
            }

            // 만약 0~9번째 비트 모두 1이라면 모든 숫자를 본 것이므로 while문을 탈출한다.
            if (!(num_bit ^ ALL_NUM)) {
                break;
            }

            ++k;
        }
        
        cout << "#" << test_case << " " << N * k << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}