
/*Test Data 
*/

/*var JSONObject={{JSONObject|safe}};*/
/*Test Data End*/
/*function $$(id){
return document.getElementById(id);
}*/
//Item ID 字典
var coldata={};

function $$(id){
        return document.getElementById(id);
        }
 
let i = 0, j = 0;
let ItemNum =0;
/*生成表格函数->for 避免表格鼠标悬浮窗不随滚动条变化*/
function CreateTable(row,col,mouse,column){
   var tab = "";
   for(let i=0;i<row;i++){
          if(i==0){
            tab+="<thead><tr>"
          }

          
          if(i!=0){
          tab += "<tr >"}
           for(let j=0;j<col;j++){


             var xuhao = ('x'+i+'y'+j).toString();
               ItemNum=(i*row+j);
                /*console.log(xuhao);*/
                  //这里加入了id 排好了序
                if(i==0||j==0){
                  if(j==0){
                      if(i==0&&j==0){
                        tab+="<td id="+xuhao+" style='width:280px;min-height:80px;max-height:80px;height:80px;'></td>";
                        continue;
                      }
                      tab+="<th id="+xuhao+column+" style='min-width:280px;width:280px;height:100px;word-wrap:break-word;'"+mouse+"></th>";
                       continue;
                      }
                  tab+="<th id="+xuhao+" '></th>";
                  continue;

                  }
                  tab+="<td id="+xuhao+" ></td>";
              }
                 if(i==0){
                 tab+="</tr></thead>"
           }
                if(i>=1&&i<(row-1)){
                 tab += "</tr>"}
                if(i==(row-1)){
                  tab += "</tr>"
                }
            }
            return tab;
}

/*函数结束*/



 function line(JSONObject){

       /* console.log("line");*/
        /*显示指定行列*/

       //删除上次存下来的item id
         for (var key in coldata) {
               delete coldata[key];
            };


        $("table").empty();
        var row=JSONObject.x,col=JSONObject.y; //获取行列的长度的变量
        var table_1=$('#table').clone(true);
       /* console.log(table_1);*/
        var tab=CreateTable(row,col,' ','');
        var tab1=CreateTable(row,col,"onmouseout=out(this) onmouseover=over(this)","col");

            table_1.attr("id","table_1");
            $$("table").innerHTML = tab;


            table_1.append(tab1);


            /*console.log("line1");

            */
            /*显示结束*/



           /* fixtable start*/


            /* $(document).ready(function(){*/
              var table = $("table");
             /* var table_col = $("#table_1");*/
              var tableId = table.attr('id');
              var tableId_col = table_1.attr('id');
              var freezeRowNum = table.attr('freezeRowNum');
              var freezeColumnNum = table.attr('freezeColumnNum');
               /*console.log(table);*/
              /*console.log(pageWidth(),pageHeight());*/
              /*根据屏幕缩放改变的table大小*/
             /* console.log($('#table_tableHead').attr('height'));*/



              /*根据屏幕缩放改变的table大小--结束*/

              if (typeof(freezeRowNum) != 'undefined' || typeof(freezeColumnNum) != 'undefined') {
                  freezeTable(table,table_1,tableId_col, freezeRowNum || 0, freezeColumnNum || 0, $('#TableSize').outerWidth(true), $('#TableSize').outerHeight(true));
                 /* console.log($('#TableSize').outerHeight(true),$('#TableSize').outerWidth(true),$('#table_tableData').outerHeight(true),$('#table_tableData').outerWidth(true));*/
                  var flag = false;

              }
              var title0="<div style='width: 100%;height:80px;backgound-color:#B0C4DE;'><canvas style='width: 100%;height: 100% ;backgound-color:#FFDC35'id='mycanvas' cellpadding='0'cellspacing='0'></canvas></div>"

                     ;
                     /* $('#table').fixedHeaderTable({});*/
                      $$("x0y0").innerHTML = title0;



                      var myCanvas = document.getElementById("mycanvas");
                      var width = myCanvas.width;
                      var height = myCanvas.height;
                      var ctx = myCanvas.getContext("2d");
                      ctx.strokeStyle="#000";
                      ctx.lineWidth=2;

                      ctx.moveTo(0,0);
                      ctx.lineTo(width,height);
                      ctx.stroke();

                      ctx.font="38px bold SimHei";
                      ctx.fontheight="bold";
                      ctx.fillText("Units",width/3*1.8,height*5/12);
                      ctx.fillText("Item",width/9,height/5*4);


                  /*测试数据*/
            for(var i in JSONObject){

              if(i!='x'&&i!='y'&&i.toString().slice(0,3)!="x0y0"){
                if(i.toString().slice(-2)=="y0"){

                    i_col=$("#"+i).attr("id");
                    var newitem=JSONObject[i].slice(11);
                    //console.log("158",newitem);

                  $(eval(i_col+"col")).append("<center><span>"+newitem.split(',')[0] +"</span><br><span style='color:#FFDEAD;'>"+newitem.split(',')[1]+"</span></center>");

                  coldata[i_col+"col"]=JSONObject[i].slice(0,11);
                   /*$$(i_col.toString()).innerHTML="<center><span>"+JSONObject[i]+"</span></center>";*/
                  }

                else{


                     /*$$(i).innerHTML="<center><span>"+JSONObject[i]+"</span></center>";*/
                     $(eval(i)).append("<center><span>"+JSONObject[i]+"</span></center>");
                     //   if (JSONObject[i]>=5&&i.toString().slice(1,2)!="0"){
                     //     $(eval(i)).css({"background": "red"});
                     // }


                 }
              }
            }
            /*测试数据*/

    /*      });*/
           /* fixtable end*/

        }
        /*
 * 锁定表头和列
 *
 * 参数定义
 *     table - 要锁定的表格元素或者表格ID
 *     freezeRowNum - 要锁定的前几行行数，如果行不锁定，则设置为0
 *     freezeColumnNum - 要锁定的前几列列数，如果列不锁定，则设置为0
 *     width - 表格的滚动区域宽度
 *     height - 表格的滚动区域高度
 */
function freezeTable(table,table_col,tableId_col,freezeRowNum, freezeColumnNum, width, height) {

    if (typeof(freezeRowNum) == 'string')
        freezeRowNum = parseInt(freezeRowNum)

    if (typeof(freezeColumnNum) == 'string')
        freezeColumnNum = parseInt(freezeColumnNum)

    var tableId;
    if (typeof(table) == 'string') {
        tableId = table;
        table = $('#' + tableId);
    } else
        tableId = table.attr('id');

   /* var tableId_col;
    if (typeof(table_col) == 'string') {
        tableId_col = table_col;
        table = $('#' + tableId_col);
    } else
        tableId = table.attr('id');
        console.log(tableId_col);*/

    var divTableLayout = $("#" + tableId + "_tableLayout");
   /* console.log(divTableLayout);*/

   /* if (divTableLayout.length != 0) {
        divTableLayout.before(table);
        divTableLayout.empty();
    } else {*/
        table.after("<div id='" + tableId + "_tableLayout' style='overflow-x:auto;height:" + $('#TableSize').outerHeight(true) + "px; width:" + width + "px;'  ></div>");

        divTableLayout = $("#" + tableId + "_tableLayout");
  /*  }*/

    var html = '';
    if (freezeRowNum > 0 && freezeColumnNum > 0)
        html += '<div id="' + tableId + '_tableFix" style="padding: 0px;height:60px;"></div>';

    if (freezeRowNum > 0)
        html += '<div id="' + tableId + '_tableHead" style="padding: 0px;"></div>';

    if (freezeColumnNum > 0)
        html += '<div id="' + tableId + '_tableColumn" style="padding: 0px;"></div>';

    html += '<div id="' + tableId + '_tableData" style="padding: 0px;"></div>';


    $(html).appendTo("#" + tableId + "_tableLayout");

    var divTableFix = freezeRowNum > 0 && freezeColumnNum > 0 ? $("#" + tableId + "_tableFix") : null;
    var divTableHead = freezeRowNum > 0 ? $("#" + tableId + "_tableHead") : null;
    var divTableColumn = freezeColumnNum > 0 ? $("#" + tableId + "_tableColumn") : null;
    var divTableData = $("#" + tableId + "_tableData");
    //console.log(table);
    //console.log(table_col);
    divTableData.append(table);

    if (divTableFix != null) {
        var tableFixClone = table.clone(true);
        tableFixClone.attr("id", tableId + "_tableFixClone");
       /* console.log(tableFixClone);*/
        divTableFix.append(tableFixClone);
    }

    if (divTableHead != null) {
        var tableHeadClone = table.clone(true);
        tableHeadClone.attr("id", tableId + "_tableHeadClone");

        divTableHead.append(tableHeadClone);
    }

    if (divTableColumn != null) {
        var tableColumnClone =  table_col.clone(true);
        tableColumnClone.attr("id", tableId + "_tableColumnClone");
       /* console.log(tableColumnClone);*/
        divTableColumn.append(tableColumnClone);
        /*console.log(document.getElementsByTagName("#tableColumnClone"));*/
    }

    $("#" + tableId + "_tableLayout table").css("margin", "0");

    if (freezeRowNum > 0) {
        var HeadHeight = 0;
        var ignoreRowNum = 0;
        $("#" + tableId + "_tableHead tr:lt(" + freezeRowNum + ")").each(function () {
            if (ignoreRowNum > 0)
                ignoreRowNum--;
            else {
                var td = $(this).find('td:first, th:first');
                HeadHeight += td.outerHeight(true);

                ignoreRowNum = td.attr('rowSpan');
                if (typeof(ignoreRowNum) == 'undefined')
                    ignoreRowNum = 0;
                else
                    ignoreRowNum = parseInt(ignoreRowNum) - 1;
            }
        });
        HeadHeight += 2;

        divTableHead.css("height", HeadHeight);
        divTableFix != null && divTableFix.css("height", HeadHeight);
    }

    if (freezeColumnNum > 0) {
        var ColumnsWidth = 0;
        var ColumnsNumber = 0;
        $("#" + tableId + "_tableColumn tr:eq(" + freezeRowNum + ")").find("td:lt(" + freezeColumnNum + "), th:lt(" + freezeColumnNum + ")").each(function () {
            if (ColumnsNumber >= freezeColumnNum)
                return;

            ColumnsWidth += $(this).outerWidth(true);

            ColumnsNumber += $(this).attr('colSpan') ? parseInt($(this).attr('colSpan')) : 1;
        });
        ColumnsWidth += 2;

        divTableColumn.css("width",'280px');
        divTableFix != null && divTableFix.css("width", '280px');
    }

    divTableData.scroll(function () {
        divTableHead != null && divTableHead.scrollLeft(divTableData.scrollLeft());

        divTableColumn != null && divTableColumn.scrollTop(divTableData.scrollTop());

    });

    var srollwidth=(myBrowser()=="Chrome")?(window.innerWidth - document.body.clientWidth):17;
    divTableFix != null && divTableFix.css({ "overflow": "hidden", "position": "absolute", "z-index": "50" });
    divTableHead != null && divTableHead.css({ "overflow": "hidden","height":$('#table_tableFix').outerHeight(true), "width": $('#TableSize').outerWidth(true)-srollwidth, "position": "absolute", "z-index": "45" });
    divTableColumn != null && divTableColumn.css({ "overflow": "hidden", "height": $('#TableSize').outerHeight(true)-srollwidth,"width":$('#table_tableFix').outerWidth(true), "position": "absolute", "z-index": "40" });
    divTableData.css({ "overflow": "scroll", "width":$('#TableSize').outerWidth(true), "height": $('#TableSize').outerHeight(true), "position": "absolute" });
    /*console.log(width,height);*/

    divTableFix != null && divTableFix.offset(divTableLayout.offset());
    divTableHead != null && divTableHead.offset(divTableLayout.offset());
    divTableColumn != null && divTableColumn.offset(divTableLayout.offset());
    divTableData.offset(divTableLayout.offset());
    /*console.log(tableHeadClone)*/


}




 /*鼠标悬停功能*/
      var differentindex=999;

      function openMsg(obj) {
          differentindex = layer.tips(coldata[obj],"#"+obj,
           {tips: [4, "#4794ec"]
         });
        }


     function over(obj){
      if($("#"+obj.id).children().length>0){    //判断是否存在子节点（若有子节点，显示悬浮窗，反之则无）
            openMsg(obj.id); //显示悬浮窗
           //console.log(obj.id);
          }
     } 
     function out(obj){
        layer.close(differentindex);
     }       

      /*鼠标悬停功能*/
     //chrome or ie
    function myBrowser(){

    var userAgent = navigator.userAgent; //取得浏览器的userAgent字符串
        //console.log(userAgent);

    var isOpera = userAgent.indexOf("Opera") > -1;

    if (isOpera) {

        return "Opera"

    }; //判断是否Opera浏览器

    if (userAgent.indexOf("Firefox") > -1) {

        return "FF";

    } //判断是否Firefox浏览器

    if (userAgent.indexOf("Chrome") > -1&&userAgent.indexOf("Edge") <= -1){

        return "Chrome";

    }
    if (userAgent.indexOf("Edge") > -1){

        return "Edge";

    }

    if (userAgent.indexOf("Safari") > -1) {

        return "Safari";

    } //判断是否Safari浏览器

    if (userAgent.indexOf("compatible") > -1 && userAgent.indexOf("MSIE") > -1 && !isOpera) {

        return "IE";

    }; //判断是否IE浏览器

}


$(document).ready(function(){



 /* test*/
/* console.log(navigator.userAgent.indexOf("Chrome"));
 console.log(navigator.userAgent.indexOf("ie"));*/

/*$("#tt").click(function(){
  console.log("IINE1")

$("#table_tableLayout").empty();
if($("#table_tableLayout").length > 0) {
    $("#TableSize").empty();
}
line();
});*/




$(window).resize(function(){
  var myBrowsertype =myBrowser();
    if(myBrowsertype=="Chrome"){
      var scrollwidth=window.innerWidth - document.body.clientWidth;
      $('#table_tableHead').css({"width":$('#TableSize').outerWidth(true)-scrollwidth});
      $('#table_tableColumn').css({"height":$('#TableSize').outerHeight(true)-scrollwidth});
      $('#table_tableData').css({"width":$('#TableSize').outerWidth(true)});
      $('#table_tableData').css({"height":$('#TableSize').outerHeight(true)});
      //console.log("Chrome",scrollwidth);
    }
    else{
      $('#table_tableHead').css({"width":$('#TableSize').outerWidth(true)-17});
      $('#table_tableColumn').css({"height":$('#TableSize').outerHeight(true)-17});
      $('#table_tableData').css({"width":$('#TableSize').outerWidth(true)});
      $('#table_tableData').css({"height":$('#TableSize').outerHeight(true)});
      //console.log("other browser");
    }

    });

/*
 * 调整锁定表的宽度和高度，这个函数在resize事件中调用
 * 
 * 参数定义
 *     table - 要锁定的表格元素或者表格ID
 *     width - 表格的滚动区域宽度
 *     height - 表格的滚动区域高度
 */
function adjustTableSize(table, width, height) {
    var tableId;
    if (typeof(table) == 'string')
        tableId = table;
    else
        tableId = table.attr('id');
    
    $("#" + tableId + "_tableLayout").width(width).height(height);
    $("#" + tableId + "_tableHead").width(width );
    $("#" + tableId + "_tableColumn").height(height);
    $("#" + tableId + "_tableData").width(width).height(height);
}
/*end*/

// start();
//
// function start(){
// $.ajax({
//   url:"/dashboard-units/",
//   type:"GET",
//   dataType:"json",
//   async:true,
//   /*data:{project:$('#project').val(),Phase:$('#Phase').val(),csrfmiddlewaretoken:'{{ csrf_token  }}'},*/
//   data:{csrfmiddlewaretoken:$("input:first").val()},
//   /*header:{'X-CSRFtoken':csrftoken},*/
//   error:function(data){
//     console.log(data);
//   },
//   success:function(data){
//      console.log(data);
//
//     $('#TableSize').empty();
//     $("#TableSize").append("<table  border='3' cellpadding='0' cellspacing='0' id='table' freezeRowNum='1' freezeColumnNum='1' overflow='scroll' class=table7_7></table>");
//       line(data);
//
//
//   }
//  })
// }

  
$('#tt').bind('click', function() {
   /* e.preventDefault();*/
    /*console.log(JSONObject);*/
    //console.log("123");
   /* var csrftoken = $.cookie('csrftoken');*/
   /* $('#TableSize').empty();
    $("#TableSize").append("<table  border='3' cellpadding='0' cellspacing='0' id='table' freezeRowNum='1' freezeColumnNum='1' overflow='scroll' ></table>");
      line(); */
      
  /* if($('#table_tableLayout'))
   
    */
   /* $('#table_tableLayout').empty();*/

/*AJAX Data*/
/*界面初始化*/

/*局部提交，刷新表格数据*/

$.ajax({
  url:"/dashboard-units/",
  type:"POST",
  dataType:"json",
  async:true,
  /*data:{project:$('#project').val(),Phase:$('#Phase').val(),csrfmiddlewaretoken:'{{ csrf_token  }}'},*/
  data:{Customer:$('#Customer').val(),project:$('#project').val(),Phase:$('#Phase').val(),csrfmiddlewaretoken:$("input:first").val(),},
  /*header:{'X-CSRFtoken':csrftoken},*/
  success:function(data){
    // console.log(data);
     
    $('#TableSize').empty();
    $("#TableSize").append("<table  border='3' cellpadding='0' cellspacing='0' id='table' freezeRowNum='1' freezeColumnNum='1' overflow='scroll' class=table7_7></table>");
      line(data); 
     
      
  },
  error:function(data){
    alert("未查询到数据，请确认查询信息");
  }
})

/*AJAX Data*/
/*表格自适应大小*/

/*表格自适应大小*/


   
  });

});
  

/*Test*/




/*Test End
*/

