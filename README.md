밑의 문제들은 시간이 지나면 다시 풀어보자.
## 효율적으로 푼 문제
- 백준 1956(운동)
  > [1956.py](https://github.com/nhlee98/Algorithm_Problem/blob/main/Baekjoon/단계별로풀어보기/32_최단경로/1956.py)   
  > pypy3로 속도에서 전체 2등을 했습니다.   
  > 힙으로 구현한 다익스트라에 백트래킹을 혼합해서 풀었습니다.   
- 프로그래머스 87946(피로도)
  > [87946.py](https://github.com/nak-honest/Algorithm_Study/blob/main/9th_Algorithm_Study/Programmers_87946/87946.py)
  > 대부분의 풀이와 다르게 dp를 이용해서 효율적으로 문제를 풀었습니다.
- 프로그래머스 42842(카펫)
  > [42842.py](https://github.com/nak-honest/Algorithm_Study/blob/main/9th_Algorithm_Study/Programmers_42842/42842.py)
  > 이분탐색을 이용해 약수를 구하는 것보다 효율적으로 문제를 풀었습니다.
- 프로그래머스 42583(다리를 지나는 트럭)
  > 트럭이 없음을 0으로 표현하면 불필요하게 0을 집어넣는데 시간이 많이 쓰입니다.
  > 따라서 다리에 트럭이 들어갈 수 없다면 0을 집어넣는 대신
  > 한번에 시간을 건너 뜀으로써 시간을 많이 단축했습니다.

## 어려웠던 문제
- 백준 10989(수 정렬하기3)
  > [10989.py](https://github.com/nhlee98/Algorithm_Problem/blob/main/Baekjoon/%EB%8B%A8%EA%B3%84%EB%B3%84%EB%A1%9C%ED%92%80%EC%96%B4%EB%B3%B4%EA%B8%B0/13_%EC%A0%95%EB%A0%AC/10989.py)  
- 백준 17103(골드바흐 파티션)
  > [17103.py](https://github.com/nhlee98/Algorithm_Problem/blob/main/Baekjoon/%EB%8B%A8%EA%B3%84%EB%B3%84%EB%A1%9C%ED%92%80%EC%96%B4%EB%B3%B4%EA%B8%B0/15_%EC%95%BD%EC%88%98_%EB%B0%B0%EC%88%98_%EC%86%8C%EC%88%982/17103.py)
- 백준 9663(N-Queen)
  > [9663.py](https://github.com/nhlee98/Algorithm_Problem/blob/main/Baekjoon/%EB%8B%A8%EA%B3%84%EB%B3%84%EB%A1%9C%ED%92%80%EC%96%B4%EB%B3%B4%EA%B8%B0/22_%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9/9663.py)   
- 백준 2580(스도쿠)
  > [2580.py](https://github.com/nhlee98/Algorithm_Problem/blob/main/Baekjoon/%EB%8B%A8%EA%B3%84%EB%B3%84%EB%A1%9C%ED%92%80%EC%96%B4%EB%B3%B4%EA%B8%B0/22_%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9/2580.py)   
- 백준 1149(RGB거리)
  > [1149.py](https://github.com/nhlee98/Algorithm_Problem/blob/main/Baekjoon/%EB%8B%A8%EA%B3%84%EB%B3%84%EB%A1%9C%ED%92%80%EC%96%B4%EB%B3%B4%EA%B8%B0/23_%EB%8F%99%EC%A0%81_%EA%B3%84%ED%9A%8D%EB%B2%951/1149.py)   
- 백준 2565(전깃줄)
  > [2565.py](https://github.com/nak-honest/Algorithm_Problem/blob/main/Baekjoon/%EB%8B%A8%EA%B3%84%EB%B3%84%EB%A1%9C%ED%92%80%EC%96%B4%EB%B3%B4%EA%B8%B0/23_%EB%8F%99%EC%A0%81_%EA%B3%84%ED%9A%8D%EB%B2%951/2565.py)   
- 백준 9251(LCS)
  > [9251.py](https://github.com/nak-honest/Algorithm_Problem/blob/main/Baekjoon/%EB%8B%A8%EA%B3%84%EB%B3%84%EB%A1%9C%ED%92%80%EC%96%B4%EB%B3%B4%EA%B8%B0/23_%EB%8F%99%EC%A0%81_%EA%B3%84%ED%9A%8D%EB%B2%951/9251.py)
- 백준 12865(평범한 배낭)
  > [12865.py](https://github.com/nak-honest/Algorithm_Problem/blob/main/Baekjoon/단계별로풀어보기/23_동적_계획법1/12865.py)
- 백준 11401(이항 계수 3)
  > [11401.py](https://github.com/nak-honest/Algorithm_Problem/blob/main/Baekjoon/단계별로풀어보기/26_분할_정복/11401.py)
- 백준 11444(피보나치 수 6)
  > [11444.py](https://github.com/nak-honest/Algorithm_Problem/blob/main/Baekjoon/단계별로풀어보기/26_분할_정복/11444.py)
- SWEA 1855(영준이의 진짜 BFS)
  > [1855.cpp](https://github.com/nak-honest/Algorithm_Problem/blob/main/SWEA/day_04/1855.cpp)   
   
## 복잡하게 푼 문제
- 백준 11005(진법 변환2)
  > [11005.py](https://github.com/nhlee98/Algorithm_Problem/blob/main/Baekjoon/%EB%8B%A8%EA%B3%84%EB%B3%84%EB%A1%9C%ED%92%80%EC%96%B4%EB%B3%B4%EA%B8%B0/8_%EC%9D%BC%EB%B0%98%EC%88%98%ED%95%991/11005.py)   
- 백준 1463(1로 만들기)
  > [1463.py](https://github.com/nhlee98/Algorithm_Problem/blob/main/Baekjoon/%EB%8B%A8%EA%B3%84%EB%B3%84%EB%A1%9C%ED%92%80%EC%96%B4%EB%B3%B4%EA%B8%B0/23_%EB%8F%99%EC%A0%81_%EA%B3%84%ED%9A%8D%EB%B2%951/1463.py)   
- 백준 11660(구간 합 구하기 5)
  > [11660.py](https://github.com/nak-honest/Algorithm_Problem/blob/main/Baekjoon/단계별로풀어보기/24_누적합/11660.py)   
- 백준 1629(곱셈)
  > [1629.py](https://github.com/nak-honest/Algorithm_Problem/blob/main/Baekjoon/단계별로풀어보기/26_분할_정복/1629.py)   
