#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int lot1, lot2;

struct relationship {
	char c;
	int a;
	int b;
};

bool cheak_duplication(vector<vector<int>>& Rvec, int a);
void find_and_add(vector<vector<int>>& Rvec, int a, int b);
int change(int a);

int main() {
	int n, m;
	int k;
	relationship rs;
	vector<relationship> rsVec;
	vector<vector<int>> FVec, EVec;
	int FVec_size = 0;

	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> rs.c >> rs.a >> rs.b;
		rsVec.push_back(rs);
	}



	for (int i = 0; i < m; i++) {
		if (rsVec[i].c == 'F') {
			if (cheak_duplication(FVec, rsVec[i].a) && cheak_duplication(FVec, rsVec[i].b)) {
				k = lot1;
				cheak_duplication(FVec, rsVec[i].a);
				if (k != lot1) {
					FVec[k].insert(FVec[k].end(), FVec[lot1].begin(), FVec[lot1].end());
					FVec.erase(FVec.begin() + lot1);
				}
				
				continue;
			}
			else if (!cheak_duplication(FVec, rsVec[i].a) && !cheak_duplication(FVec, rsVec[i].b)) {
				FVec.push_back({ rsVec[i].a, rsVec[i].b });
				continue;
			}

			if (cheak_duplication(FVec, rsVec[i].a)) {
				FVec[lot1].push_back(rsVec[i].b);
			}
			else FVec.push_back({ rsVec[i].a });

			if(cheak_duplication(FVec, rsVec[i].b)) {
				FVec[lot1].push_back(rsVec[i].a);
			}
			else FVec.push_back({ rsVec[i].b });

		}
		else if(rsVec[i].c == 'E'){
			if (cheak_duplication(EVec, rsVec[i].a)) {
				find_and_add(FVec, EVec[lot1][change(lot2)], rsVec[i].b);
			}
			else if (cheak_duplication(EVec, rsVec[i].b)) {
				find_and_add(FVec, EVec[lot1][change(lot2)], rsVec[i].a);
			}

			EVec.push_back({ rsVec[i].a, rsVec[i].b });
		}
	}

	for (int i = 1; i <= n; i++) {
		if (cheak_duplication(FVec, i)) continue;
		else {
			FVec.push_back({ i });
		}
	}


	//for (int i = 0; i < FVec.size(); i++) {
	//	for (int j = 0; j < FVec[i].size(); j++) {
	//		cout << FVec[i][j] << " ";
	//	}
	//	cout << "\n";
	//}

	cout << FVec.size();
}

bool cheak_duplication(vector<vector<int>> &Rvec, int a) {
	for (int i = 0; i < Rvec.size(); i++) {
		for (int j = 0; j < Rvec[i].size(); j++) {
			if (Rvec[i][j] == a) {
				lot1 = i;
				lot2 = j;
				return 1;
			}
		}
	}
	return 0;

}

void find_and_add(vector<vector<int>> &Rvec, int a, int b) {
	for (int i = 0; i < Rvec.size(); i++) {
		for (int j = 0; j < Rvec[i].size(); j++) {
			if (Rvec[i][j] == a) {
				Rvec[i].push_back(b);
				return;
			}
			else if (Rvec[i][j] == b) {
				Rvec[i].push_back(a);
				return;
			}
		}
	}
	Rvec.push_back({ a, b });
}

int change(int a) {
	if (a == 0) return a = 1;
	else return a = 0;
}
