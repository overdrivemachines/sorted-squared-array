#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> sortedSquaredArray(vector<int> array) {
  vector<int> result;
  if (array.size() == 0) return {};

  sort(array.begin(), array.end());

  for (int num : array) {
    result.push_back(num * num);
  }
  return result;
}

void printV(vector<int> array) {
  for (int i : array) {
    cout << i << " ";
  }
  cout << endl;
}

int main(int argc, char const *argv[]) {
  vector<int> array = {3, 2};
  printV(sortedSquaredArray(array));
  return 0;
}
