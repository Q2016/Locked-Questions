/*overlap of 2 interval a b is (max(a0, b0), min(a1, b1))
detail is in: https://discuss.leetcode.com/topic/111198
*/

class MyCalendar {
    vector<pair<int, int>> books;
public:    
    bool book(int start, int end) {
        for (pair<int, int> p : books)
            if (max(p.first, start) < min(end, p.second)) return false;
        books.push_back({start, end});
        return true;
    }
};
