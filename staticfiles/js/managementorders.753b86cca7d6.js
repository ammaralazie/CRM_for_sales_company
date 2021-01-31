var form=document.forms
for(var i=0 ;i<form.length;i++){
    if (form[i].className == 'form_state'){
        len=form[i].children.length
       for(var j=0;j<len;j++){
           
            form[i].children[j].addEventListener('click',function(e){ 
                this.children[0].classList.toggle('checkmark')
                action=this.children[0].classList[0]
                product=this.children[0].dataset.product
                customer=this.children[0].dataset.customer
                managementorder(action,product,customer)

            })
       }//end for j
    }//end if
}//end for form


function  managementorder(action,product,customer){
    var url='/product/mangement/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json','X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'action':action,'product':product,'customer':customer})
    })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        console.log(data)
        window.location.reload()
        console.log(location)
    })
}//end function managementorder