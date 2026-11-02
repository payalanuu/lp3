
#include <iostream>
#include <queue>
using namespace std;

// Create a node
struct Node
{
    char ch;
    int freq;

    Node *left, *right;

    Node(char c, int f)
    {
        ch = c;
        freq = f;
        left = right = NULL;
    }
};

// Compare frequencies
struct Compare
{
    bool operator()(Node* a, Node* b)
    {
        return a->freq > b->freq;
    }
};

// Print Huffman codes
void printCode(Node* root, string code)
{
    if (root == NULL)
        return;

    // If leaf node, print character and code
    if (root->left == NULL && root->right == NULL)
    {
        cout << root->ch << " : " << code << endl;
        return;
    }

    printCode(root->left, code + "0");
    printCode(root->right, code + "1");
}

int main()
{
    char ch[] = {'A', 'B', 'C', 'D', 'E', 'F'};
    int freq[] = {5, 9, 12, 13, 16, 45};

    int n = 6;

    // Create priority queue
    priority_queue<Node*, vector<Node*>, Compare> pq;

    // Insert characters with frequencies
    for (int i = 0; i < n; i++)
    {
        pq.push(new Node(ch[i], freq[i]));
    }

    // Build Huffman tree using greedy method
    while (pq.size() > 1)
    {
        Node* left = pq.top();
        pq.pop();

        Node* right = pq.top();
        pq.pop();

        Node* newNode = new Node('$',
                                left->freq + right->freq);

        newNode->left = left;
        newNode->right = right;

        pq.push(newNode);
    }

    // Print Huffman codes
    cout << "Huffman Codes:\n";
    printCode(pq.top(), "");

    return 0;
}
