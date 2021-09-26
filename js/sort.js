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