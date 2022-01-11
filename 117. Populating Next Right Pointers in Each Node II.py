If you have solved [https://leetcode.com/problems/populating-next-right-pointers-in-each-node/] 
this question this is exactly same as this one except for one change.

Basically this is purely level order travsersal code with slight modification for the root -> next value

You just have to think 2 things in this question.

1.How to get the last val to NULL ?.
2.How to get connect with the current node to previous one ?.

If you are able to find the ans of these two questions mentioned above then you will reach the solution
also if you are here to see the solution i would recommend you to pause for a while
and think about these questions i am sure you willl find the ans otherwise ans
is just right below you can see anytime you want just give it a though for a whlle.



if(root == NULL) return NULL;
        queue<Node*> q;
        q.push(root);
        while(!q.empty()){
            int size = q.size(); // get size of queue 
            for(int i=0 ; i < size ; i++){
                Node* item = q.front(); 
                if(size - 1 == i) // checking the last value of the level
                     item -> next = NULL; 
                
                q.pop();
                
                if(size - 1 != i) // if this is not the last value then previous value will point to next one
                     item -> next = q.front(); 
                
                if(item -> left != NULL)
                    q.push(item -> left);
                if(item -> right != NULL)
                    q.push(item -> right);
            }
        } 
        return root;
