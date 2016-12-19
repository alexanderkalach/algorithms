#include <stdio.h>

void quicksort(int nums[], int s, int e);
int quicksort_partition(int nums[], int s, int e);

int main()
{
	int nums[] = {6, 7, 2, 10, 3, 14};
	quicksort(nums, 0, 5);

	for (int i = 0; i < 6; i++) {
		printf("%d ", nums[i]);
	}
}

void quicksort(int nums[], int s, int e)
{
	if (s < e) {
		int q = quicksort_partition(nums, s, e);
		quicksort(nums, s, q - 1);
		quicksort(nums, q + 1, e);
	}
}

int quicksort_partition(int nums[], int s, int e)
{
	int t;
	int x = nums[e];
	int i = s - 1;
	for (int j = s; j <= e - 1; j++) {
		if (nums[j] <= x) {
			i++;
			t = nums[i];
			nums[i] = nums[j];
			nums[j] = t;
		}
	}
	t = nums[i + 1];
	nums[i + 1] = nums[e];
	nums[e] = t;

	return i + 1;
}