/*Test Data
*/
/*Test Data End*/
/*function $$(id){
return document.getElementById(id);
}*/
  function $$(id){
        return document.getElementById(id);
        }

let i = 0, j = 0;
let ItemNum =0;

 function line(JSONObject){

       /* console.log("line");*/
        /*显示指定行列*/
        $("table").empty();
        var row=JSONObject.x,col=JSONObject.y; //获取行列的长度的变量
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

                if(i==0||j==0){
                  if(j==0){
                      if(i==0&&j==0){
                        tab+="<td id="+xuhao+" style='min-width:200px;min-height:60px;max-height:60px;height:60px;'></td>";
                        continue;
                      }
                      tab+="<th id="+xuhao+" style='min-width:200px;'></th>";
                       continue;
                      }
                  tab+="<th id="+xuhao+" '></th>";
                  continue;
                //这里加入了id 排好了序
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

            $$("table").innerHTML = tab
            /*console.log("line1");
            */
            /*显示结束*/

            /*测试数据*/
            for(var i in JSONObject){
              /*console.log(i);*/
              if(i!='x'&&i!='y'){
              $$(i).innerHTML="<center><span>"+JSONObject[i]+"</span></center>";
              if (JSONObject[i]>=5){
              $$(i).style.backgroundColor="#FF0000";
               }
             }
            }

           /* fixtable start*/


            /* $(document).ready(function(){*/
              var table = $("table");
              var tableId = table.attr('id');
              var freezeRowNum = table.attr('freezeRowNum');
              var freezeColumnNum = table.attr('freezeColumnNum');
              /*console.log(pageWidth(),pageHeight());*/
              /*根据屏幕缩放改变的table大小*/
             /* console.log($('#table_tableHead').attr('height'));*/

                 $(window).resize(function(){
                    $('#table_tableHead').css({"width":($('#TableSize').outerWidth(true)-17)});
                    $('#table_tableColumn').css({"height":($('#TableSize').outerHeight(true)-17)});
                    $('#table_tableData').css({"width":$('#TableSize').outerWidth(true)});
                    $('#table_tableData').css({"height":$('#TableSize').outerHeight(true)});
                   /* console.log($('#TableSize').outerHeight(true),$('#TableSize').outerWidth(true),$('#table_tableData').outerHeight(true),$('#table_tableData').outerWidth(true),$('#table_tableFix').outerHeight(true),);
                    */
                  });

              /*根据屏幕缩放改变的table大小--结束*/

              if (typeof(freezeRowNum) != 'undefined' || typeof(freezeColumnNum) != 'undefined') {
                  freezeTable(table, freezeRowNum || 0, freezeColumnNum || 0, $('#TableSize').outerWidth(true), $('#TableSize').outerHeight(true));
                 /* console.log($('#TableSize').outerHeight(true),$('#TableSize').outerWidth(true),$('#table_tableData').outerHeight(true),$('#table_tableData').outerWidth(true));*/
                  var flag = false;

              }
              var title0="<div style='width: 100%;height:60px;backgound-color:#B0C4DE;'><canvas style='width: 100%;height: 100% ;backgound-color:#FFDC35'id='mycanvas' cellpadding='0'cellspacing='0'></canvas></div>"

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
function freezeTable(table, freezeRowNum, freezeColumnNum, width, height) {
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

    divTableData.append(table);

    if (divTableFix != null) {
        var tableFixClone = table.clone(true);
        tableFixClone.attr("id", tableId + "_tableFixClone");
        divTableFix.append(tableFixClone);
    }

    if (divTableHead != null) {
        var tableHeadClone = table.clone(true);
        tableHeadClone.attr("id", tableId + "_tableHeadClone");
        divTableHead.append(tableHeadClone);
    }

    if (divTableColumn != null) {
        var tableColumnClone = table.clone(true);
        tableColumnClone.attr("id", tableId + "_tableColumnClone");
        divTableColumn.append(tableColumnClone);
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

        divTableColumn.css("width", ColumnsWidth);
        divTableFix != null && divTableFix.css("width", ColumnsWidth);
    }

    divTableData.scroll(function () {
        divTableHead != null && divTableHead.scrollLeft(divTableData.scrollLeft());

        divTableColumn != null && divTableColumn.scrollTop(divTableData.scrollTop());

    });


    divTableFix != null && divTableFix.css({ "overflow": "hidden", "position": "absolute", "z-index": "50" });
    divTableHead != null && divTableHead.css({ "overflow": "hidden","height":$('#table_tableFix').outerHeight(true), "width": $('#TableSize').outerWidth(true)-17, "position": "absolute", "z-index": "45" });
    divTableColumn != null && divTableColumn.css({ "overflow": "hidden", "height": $('#TableSize').outerHeight(true)-17,"width":$('#table_tableFix').outerWidth(true), "position": "absolute", "z-index": "40" });
    divTableData.css({ "overflow": "auto", "width":$('#TableSize').outerWidth(true), "height": $('#TableSize').outerHeight(true), "position": "absolute" });
    /*console.log(width,height);*/

    divTableFix != null && divTableFix.offset(divTableLayout.offset());
    divTableHead != null && divTableHead.offset(divTableLayout.offset());
    divTableColumn != null && divTableColumn.offset(divTableLayout.offset());
    divTableData.offset(divTableLayout.offset());
    /*console.log(tableHeadClone)*/
      /*$$('table_tableHead').style.backgroundColor="#FFDC35";
       $$('table_tableColumn').style.backgroundColor="#FF0000";
       $$('table_tableFix').style.backgroundColor="#FFF";*/

}

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
    $("#" + tableId + "_tableHead").width(width - 17);
    $("#" + tableId + "_tableColumn").height(height - 17);
    $("#" + tableId + "_tableData").width(width).height(height);
}


$(document).ready(function(){
/*$("#tt").click(function(){
  console.log("IINE1")

$("#table_tableLayout").empty();
if($("#table_tableLayout").length > 0) {
    $("#TableSize").empty();
}
line();
});*/

$('#tt').bind('click', function() {
   /* e.preventDefault();*/
    /*console.log(JSONObject);*/
    console.log("123");

   /* $('#TableSize').empty();
    $("#TableSize").append("<table  border='3' cellpadding='0' cellspacing='0' id='table' freezeRowNum='1' freezeColumnNum='1' overflow='scroll' ></table>");
      line(); */

  /* if($('#table_tableLayout'))

    */
   /* $('#table_tableLayout').empty();*/

/*AJAX Data*/
/*局部提交，刷新表格数据*/

$.ajax({
  url:"/dashboard-units/",
  type:"POST",
  dataType:"json",
  async:true,/*异步先加载页面再加载动作*/
  data:{
      csrfmiddlewaretoken:$("input:first").val(),
      Customer:$('#Customer').val(),
      project:$('#project').val(),
      Phase:$('#Phase').val()},/*Ajax与后端数据交换*/
  success:function(data){
      console.log(data);
     console.log($('#project').val(),$('#Phase').val());/*Ajax从页面id获取值*/
    $('#TableSize').empty();
    $("#TableSize").append("<table  border='3' cellpadding='0' cellspacing='0' id='table' freezeRowNum='1' freezeColumnNum='1' overflow='scroll' class=table7_7></table>");
      line(data);

  },
  error:function (data) {
      console.log(data);
      console.log("fail");
  }

})



/*AJAX Data*/



  });

});


/*Test*/


function myFunction()
{
alert("Hello World!");
}

/*Test End
*/
