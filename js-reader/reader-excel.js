let getexcelData = [] // 存储excel数据
function onChange(event) {
      getexcelData = []
      var file = event.target.files[0];
      var reader = new FileReader();
      reader.onload = function(event) {
            var data = event.target.result;
            var workbook = XLSX.read(data, {type: 'binary'});
            outputWorkbook(workbook)
      }
      reader.readAsBinaryString(file);
}
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
		console.log(getexcelData,'-26')
    });
}
