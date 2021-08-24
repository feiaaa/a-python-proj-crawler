//-----------------------------------------------------------------------------
//  DialogMsgInJson.js
//-----------------------------------------------------------------------------
/*:
 * @plugindesc (v.0.0)对话内容插件
 * 把对话放在json字符串里，引用展示
 * @author feiaaa  https://gitee.com/feiaaa
 *
 */

var Fei3a = Fei3a || {}; 
(function() {
	var lang='zh-CN';
	var msg=''
　　Fei3a.change=function(l){lang=l}
　　Fei3a.setMsg=function(id){
		// JQ的方式，
		$.ajaxSettings.async = false; // 异步改同步
		$.getJSON('./locale/'+lang+'.json',data=>{
			console.log(data[id])
	      msg= data[id]
	    })
　　}// showMsgEnd
	Fei3a.getMsg=function(){
		return msg
	}
	
})()