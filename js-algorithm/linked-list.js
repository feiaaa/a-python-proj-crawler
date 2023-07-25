// 节点
class  neNode{
	constructor(data){
		this.data=data;
		this.next=null;
	}
}
// 单向链表
class singleLinkedList{
	constructor(){
		this.head=null; // 表头
	}
	// 新增到队尾
	add(data){
		let node=new neNode(data);
		if(this.head===null){
			// 空链表:直接排到队尾  O(1)
			this.head=node;
		}else{
			// 非空链表:挨个找下家，遍历到队尾为止,排到队尾O(n)
			let current=this.head;
			while(current.next){
				current=current.next;
			}
			current.next=node;
		}
	}
	//指定位置前插入节点 O(n)
	insert(data,target) {
		let node =new neNode(data);
		let current=this.head;
		while(current.next){
			if(current.data==target){
				node.next=current.next; // 新节点next指下家
				current.next=node;// 旧节点next指新节点
				break;
			}
			current=current.next;
		}
	}
	
	//查找节点O(n)
	find(data){
		let current=this.head;
		while(current){
			if(current.data==data){
				return current;
			}
			current=current.next;
		}
		return null;
	}
	// 删除节点O(n)
	remove(data){
		//需要两个指针，一个指现在，一个指前一步
		let current=this.head;
		let prev=null;
		while(current){
			if(current.data==data){
				if(prev==null){// 删的是第一项
					this.head=current.next;
				}else{ // 删的是中间项
					prev.next=current.next;
				}
				
			}
			prev=current;
			current=current.next;
		}
	}
}
const list = new singleLinkedList();
list.add(1);
list.add(2);
list.add(3);
list.insert(4, 2);
console.log(list.find(3),"==find");
list.remove(3);
console.dir(list, { depth: null });

// 双向链表