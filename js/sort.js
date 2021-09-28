var arr=[9,8,7,6]


function insertionSort(arr){
    var len=arr.length;
    var i,pre;
    for(i=1;i<len;i++){
        if(arr[i]<arr[i-1]){
            var tmp=arr[i] // 后项
            pre=i-1;//当前已经排序过的尾数
            for(pre;pre>=0 && arr[pre]>tmp;pre--){
                arr[pre+1]=arr[pre]; // 已经排序过的内部调动，交换位置

            }
            console.log(pre,'=pre')
            arr[pre+1]=tmp // 已经理完了
        }
    }


    return arr
}

insertionSort(arr)

function selectionSort(arr) {
    var len = arr.length;
    var minIndex, temp;
    for(i=0;i<len-1;i++){
        minIndex=i;
        for(var j=i+1;j<len;j++){
            if(arr[j]<arr[minIndex]){
				minIndex=j; // 找最小值的下标
			}
        }
        // 当前数 和最小数换位子
        temp=arr[i]
        arr[i]=arr[minIndex]
        arr[minIndex]=temp


    
}

// 归并两件套，需要额外空数组辅助
function mergeSort(arr){
	var len=arr.length;
	if(len<2)return arr ;//一个数不用排
	// 持续打散，稀碎到最大单位为2， 单数情况下[[1],[2,3]]
	var middle=Math.floor(len/2);
	var left=arr.slice(0,middle),right=arr.slice(middle);
	return merge(mergeSort(left),mergeSort(right)) 	
}

function merge(left,right){
	//
	
	var res=[];
	while(left.length && right.length){
		// 谁小就放谁
		if(left[0]<=right[0]){
			res.push(left.shift()) // 把left第一个数提出来,同时left的内容变了
		
		}else{
			res.push(right.shift())
		}
	}
	// 如果其中一方空了，另一方还有剩，就放进去
	while(left.length){res.push(left.shift())}
	while(right.length){res.push(right.shift())}
	return res;
}
// 希尔排序=分组+组内插入排序
function shellSort(arr){
	var len=arr.length;
	gap=len;
	for(gap;gap>0;gap=Math.floor(gap/2)){
		// 组内插入排序
		for(var i=gap;i<len;i++){
			temp=arr[i];
			for(var j=i-gap;j>=0 && arr[j]>temp;j=j-gap){
				arr[j+gap]=arr[j] //持续后移
			}
			arr[j+gap]=temp //把数字插坑里
		}
	}
	return arr
}