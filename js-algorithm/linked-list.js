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
	//更新节点
	
	//插入节点()
}
const list = new singleLinkedList();
list.add(1);
list.add(2);
list.add(3);
// list.insert(4, 2);
console.dir(list, { depth: null });


// 双向链表