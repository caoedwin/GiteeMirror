var obj={};
    Object.defineProperty(obj,'hello',{
      set:function(newVal){

         /*document.getElementById('item').value=newVal;*/
         $('#test').css({"display":"block"});
         document.getElementById("test").innerHTML="<span>Item Description:</span><br>"+newVal;
      }
    });
    // console.log('ttt');
    document.getElementById("units").addEventListener('keyup',function(e){

    console.log(e.target.value);
      if(e.target.value.length==10){
         $.ajax({
              url:"/index/",
              type:"POST",
              dataType:"JSON",
              async:true,
              /*data:{project:$('#project').val(),Phase:$('#Phase').val(),csrfmiddlewaretoken:'{{ csrf_token  }}'},*/
              data:{units:$('#units').val(),unitSearch:"unitSearch",csrfmiddlewaretoken:$("input:first").val()},
              /*header:{'X-CSRFtoken':csrftoken},*/
              error:function(data){
                console.log(data+"error");
              },
              success:function(data){
                // console.log(data.indexOf('<!DOCTYPE html>'));
                console.log(data,'suc');
                $('#customer').val(data.Customer);
                $('#phase').val(data.Phase);
                }
               })
                    }
      else{
        $('#test').empty();
      }


   });

    document.getElementById("item1").addEventListener('keyup',function(e){

    console.log(e.target.value);
      if(e.target.value.length==11){
         $.ajax({
              url:"/index/",
              type:"POST",
              dataType:"text",
              async:false,
              /*data:{project:$('#project').val(),Phase:$('#Phase').val(),csrfmiddlewaretoken:'{{ csrf_token  }}'},*/
              data:{item:$('#item1').val(),itemSearch:"itemSearch",csrfmiddlewaretoken:$("input:first").val()},
              /*header:{'X-CSRFtoken':csrftoken},*/
              error:function(data){
                console.log(data+"error");
              },
              success:function(data){
                console.log(data.indexOf('<!DOCTYPE html>'));
                if(data.indexOf('<!DOCTYPE html>')!==1){
                  obj.hello=data;
                  console.log("success");
                  }
                  else {
                   /* $("#allbody").html(data);*///????????????body?????????html
                    console.log("jump to login");
                    window.location.href="/login/";
                  }
                }
               })
                    }
      else{
        $('#test').empty();
      }


   });
    var keydownFirstTime = 0;
    function keyup(obj) {
      var date = new Date();
      var nowTime = date.getTime();
      if (obj.value.length<2) {
          keydownFirstTime = nowTime;
      }
       if(nowTime-keydownFirstTime >500){
          obj.value='';
       }
   }


    //pass and fail  confirm  alter window
     $(document).ready(function(){



      $('#pass').on('click',function(){

        layer.confirm('?????????????????????Pass?', {
          btn: ['??????','??????'] //??????
        }, function(){
          //??????????????????(?????????pass) by ajax
           $.ajax({
              url:"/index/",
              type:"POST",
              dataType:"html",
              async:true,
              /*data:{project:$('#project').val(),Phase:$('#Phase').val(),csrfmiddlewaretoken:'{{ csrf_token  }}'},*/
              data:{Customer:$('#customer').val(),Phase:$('#phase').val(),Units:$('#units').val(),item:$('#item1').val(),Comments:$('#comments').val(),PassButton:"PassButton",Result:"pass",csrfmiddlewaretoken:$("input:first").val(),},
              /*header:{'X-CSRFtoken':csrftoken},*/
              error:function(data){
                console.log(data);
              },
              success:function(data){
                   layer.msg('????????????', {icon: 1,time:1000});
                  console.log(data+"pass");
                  $('#allbody').html(data);
                }
               })


        }, function(){
          layer.msg('???????????????',{icon: 5,time:1000});
        });
       }
      )
      $('#fail').on('click',function(){

        layer.confirm('?????????????????????Fail?', {
          btn: ['??????','??????'] //??????
        }, function(){
            //??????????????????(?????????fail) by ajax
           $.ajax({
              url:"/index/",
              type:"POST",
              dataType:"html",
              async:true,
              /*data:{project:$('#project').val(),Phase:$('#Phase').val(),csrfmiddlewaretoken:'{{ csrf_token  }}'},*/
              data:{Customer:$('#customer').val(),Phase:$('#phase').val(),Units:$('#units').val(),item:$('#item1').val(),Comments:$('#comments').val(),FailButton:"FailButton",Result:"fail",csrfmiddlewaretoken:$("input:first").val(),},
              /*header:{'X-CSRFtoken':csrftoken},*/
              error:function(data){
                console.log(data);
              },
              success:function(data){
                   layer.msg('????????????', {icon: 1,time:1000});
                  console.log(data+"fail");
                  $('#allbody').html(data);
                }
               })


        }, function(){
          layer.msg('???????????????',{icon: 5,time:1000});
        });
       }
      )

    });
