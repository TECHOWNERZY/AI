# include <bits/stdc++.h>
using namespace std;



class Node{
	public :
		int val;
		Node* next;

		Node(int val){
			this->val = val;
			this->next = NULL;

		}

};


Node* takeInput(){
	Node* head = NULL;
	Node* tail = NULL;
	int val;
	cout<<"Enter the value::";
	cin>>val;
	while(val != -1){
		Node* temp = new Node(val);
		if(head == NULL){
			head = temp;
			tail = temp;
		} else {
			tail->next = temp;
			tail = temp;
		}
		cout<<"Enter the value::";
		cin>>val;

	}
	return head;
}


void printList(Node* head){
	Node* temp = head;
	while(temp != NULL){
		cout<<temp->val<<" ";
		temp = temp->next;
	}
}

void insertNode(int pos, int value, Node* head){
	if(head == NULL){
		return ;
	}
	if(pos == 0){
		Node* temp = new Node(value);
		temp->next = head;
		head = temp;
		return ;
	}

	int count = 0;
	Node* temp = head;
	while(temp != NULL){
		if(count == pos - 1){
			Node* newNode = new Node(value);
			Node* flag = temp->next;
			temp->next = newNode;
			newNode->next = flag;
			return;
		}
		temp = temp->next;
	}
}

void deleteNode(Node* head, int pos){
	if(head == NULL){
		return ;
	}
	if(pos == 0){
		Node* temp = head;
		head->next = NULL;
		return temp->next;
	}

	int count = 0;
	Node* temp = head;
	while(temp != NULL){
		if(count = pos - 1){
			Node* newNode = temp->next->next;
			Node* flag  = temp->next;
			flag->next = NULL;
			temp->next = newNode;
			return;
		}
		temp = temp->next;
	}
}


int main() {
	Node* head = takeInput();
	printList(head);


}