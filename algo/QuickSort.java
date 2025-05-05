public class QuickSort{
    public static void main(String[] args) {

        int[] arr = { 1, 1, 6, 2, 7, 9, 3, 4, 5, 1, 10, 8 };
        quickSort(arr, 0, arr.length - 1);
        printArr(arr);

    }

    static void quickSort(int[] arr, int start, int end) {
        if (start > end) {
            return;
        }
        int leftPtr = start;
        int rightPtr = end;
        int baseNumber = arr[start];
        while (leftPtr != rightPtr) {
            while (rightPtr > leftPtr && arr[rightPtr] >= baseNumber) {
                // * Move the right ptr FIRST until it finds one
                // * that is SMALLER than the base number
                // * OR it meets the left ptr
                rightPtr--;
            }
            while (leftPtr < rightPtr && arr[leftPtr] <= baseNumber) {
                // * Move the left ptr NEXT until it finds one
                // * that is GREATER than the base number
                // * OR it meets the right ptr
                leftPtr++;
            }
            // * Do the swap here
            int temp = arr[leftPtr];
            arr[leftPtr] = arr[rightPtr];
            arr[rightPtr] = temp;
        }
        // * Now we have finished the swap
        // * Both left ptr AND right ptr are
        // * pointing to the same element now
        // * We need to SWAP the base number with the
        // * number they are pointing to.
        arr[start] = arr[leftPtr];
        arr[leftPtr] = baseNumber;
        quickSort(arr, start, leftPtr - 1);
        quickSort(arr, leftPtr + 1, end);
    }

    static void printArr(int[] arr) {
        // 3.遍历数组
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}

