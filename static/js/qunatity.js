var topu=document.getElementsByClassName('top_quantity')
var downu=document.getElementsByClassName('down_quantity')
for(var i=0;i<topu.length;i++){
    if(user != 'AnonymousUser'){
        topu[i].addEventListener('click',function(e){
            e.preventDefault()
            action=this.dataset.action
            orderId=this.dataset.orid
            qunatitiy(action,orderId)
        }//end function
        )//end event
    }//end if
}//end for

for(var i=0;i<downu.length;i++){
    if(user != 'AnonymousUser'){
        downu[i].addEventListener('click',function(e){
            e.preventDefault()
            action=this.dataset.action
            orderId=this.dataset.orid
            qunatitiy(action,orderId)
        }//end function
        )//end event
    }//end if
}//end for


function qunatitiy(action,orderId){
    var url='/product/qunatity/'
    fetch(url,{
        method:'POST',
        headers:{'Content-Type':'application/json','X-CSRFToken':csrftoken},
        body:JSON.stringify({'action':action ,'orderId':orderId})
    })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        console.log(data)
        window.location.reload()
    })

}//end function 