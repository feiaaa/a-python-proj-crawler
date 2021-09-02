// 最简单的功能
var Fei3a = Fei3a || {}; 
// 闭包=函数+函数内部能访问到的变量
(function() {
	var n=999;	
　　Fei3a.nAdd=function(){n+=1}
　　Fei3a.showMsg=function(){
　　　　console.log(n,'=20');
　　}
	
})()

// index.html调用方式
/*
Fei3a.nAdd()
Fei3a.showMsg()
*/
