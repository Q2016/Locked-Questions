Question:
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or 
move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. 
Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. 
Return the current url after forwarding in history at most steps.  




Solution:

For the picture: https://leetcode.com/problems/design-browser-history/discuss/674486/Two-Stacks-Pretty-code.  
  
It’s not difficult to realize that we need a stack so that back can be implemented. However, what to do for forward. 
Because you want the ability to visit all pages in the backward as well as the forward direction, we need to store the URLs whenever we go back. 
If you see the order in which we want to visit, you will quickly realize that we need two stacks. 
One to store history and another to store the next URLs in case we go back.  

Two special cases:
You must always have at least one element in the history stack which is the page that you are currently at.
But for the forward stack, this condition is not necessary.

  
  
  
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.future = []
        self.history.append(homepage)

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.history) > 1:
            self.future.append(self.history[-1])
            self.history.pop()
            steps -= 1
        return self.history[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.future:
            self.history.append(self.future[-1])
            self.future.pop()
            steps -= 1
        return self.history[-1]  
