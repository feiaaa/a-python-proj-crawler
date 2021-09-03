// https://github.com/SheetJS/sheetjs/tree/master/demos/xhr

let getexcelData = []; // 存储excel数据
var filePath='./locale/7.xlsx';
// (function(){
	var request = new XMLHttpRequest();
	        request.open("GET", filePath);
			request.responseType = "arraybuffer";
	        // request.overrideMimeType('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
	        console.log(request.response,'=64')
	        request.onload = function() {
	            if (request.status < 400) {
	                // var reader = new FileReader();
	                var data = new Uint8Array(request.response);
					console.log(data,'=15')
	                var workbook = XLSX.read(data, {type:"array"});
	                outputWorkbook(workbook)	
	
	            }
	        };
	        request.send();
// })()

// function onChange(event) {
//       getexcelData = []
//       var file = event.target.files[0];
//       var reader = new FileReader();
//       reader.onload = function(event) {
//             var data = event.target.result;
//             var workbook = XLSX.read(data, {type: 'binary'});
//             outputWorkbook(workbook)
//       }
//       reader.readAsBinaryString(file);
// }
// 读取 excel文件
function outputWorkbook(workbook) {
    var sheetNames = workbook.SheetNames; // 工作表名称集合
    sheetNames.forEach(name => {
        var worksheet = workbook.Sheets[name]; // 只能通过工作表名称来获取指定工作表
        for(var key in worksheet) {
            // v是读取单元格的原始值
            if (key, key[0] !== '!') {
                getexcelData.push(worksheet[key].v)
            }
        }
		console.log(getexcelData,'=26')
    });
}
