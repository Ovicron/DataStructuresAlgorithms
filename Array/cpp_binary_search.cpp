template<std::size_t N>
string binarySearch(int (&lst)[N], int target)
{
    int low = 0;
    int high = sizeof(lst) - 1;

    while (low <= high)
    {
        int mid = low + (high - low) / 2;

        if (lst[mid] == target)
        {
            return "Found";
        } else if (lst[mid] < target)
        {
            low = mid + 1;
        } else
            {
                high = mid - 1;
            }
    }
    return "No target found";
};


int main()
{
    int sorted_list[] = {1,2,3,4,5, 7, 22, 43, 234, 465, 576, 967};
    cout << binarySearch(sorted_list, 40);
}
