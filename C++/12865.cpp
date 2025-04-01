#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;





int main() {
	int N;
	int inW, inV;
	int K;
	vector<int> W, V;

	int sumNum, MAX;

	cout << "물품의 수 N과 버틸 수 있는 무게 K를 입력하세요";
	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cout << "물품의 무게W과 물품의 가치 V를 입력하세요";
		cin >> inW >> inV;
		W.push_back(inW);
		V.push_back(inV);
	}

	while (sumNum <= K) {
		for (int j = 0; j < N; j++) {
			if (W[j] + W[j + 1] < K) {

			}
		}
	}



	/*
	// print
	for (int j = 0; j < W.size(); j++) {
		cout << W[j];
	}
	*/


	return 0;
}

