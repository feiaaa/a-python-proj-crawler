// 已被魔改，原文件见同名bak

let getexcelData = {}; // 存储excel数据
var filePath='./locale/7.xlsx';
(function(){
	var request = new XMLHttpRequest();
	        request.open("GET", filePath);
			request.responseType = "arraybuffer";
	        request.onload = function() {
	            if (request.status < 400) {
	                // var reader = new FileReader();
	                var data = new Uint8Array(request.response);
	                var workbook = XLSX.read(data, {type:"array"});
	                getexcelData=outputWorkbook(workbook)	
					console.log(getexcelData,'=18')
	            }
	        };
	        request.send();
})()

// 读取 excel文件
function outputWorkbook(workbook) {
	const name ='role';
	var worksheet = workbook.Sheets[name];
    
	const sheetDict={'A':'chapterId','B':'txtId','C':'roleId','D':'text'} // sheetHeader
	const excelArray=[]
	for(var key in worksheet) {
		// v是读取单元格的原始值
		if (key, key[0] !== '!') {

			const k=key.slice(0,1),i=key.slice(1,key.length);
			if(!excelArray[i-1]){
				excelArray[i-1]={}
			}
			excelArray[i-1][sheetDict[k]]=worksheet[key].v;
		}
	}
	
	const dialogObj=changeExcelArrayToObj(excelArray.slice(1,excelArray.length-1))

	return dialogObj;
	
}

function changeExcelArrayToObj(excelData=[]){
	const excelObj={}
	excelData.map(el=>{
		excelObj[el.txtId]=el
	})
	return excelObj
}
// todo Txt
function changeTxTArrayToObj(TXTDataArray=[]){
	const txtObj={}
	TXTData.map(txtString=>{
		const textObj=txtString.split(":")
		textObj[textObj[1]]={
			'chapterId':textObj[0],
			'txtId':textObj[1],
			'roleId':textObj[2],
			'text':textObj[3]
		}
	})
	return textObj
}
