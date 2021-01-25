
check=document.getElementsByClassName('div_uncomplate')
console.log('complate :',check)
for(var i=0 ;i<check.length ;i++){
    check[i].addEventListener('click',function(e){
        e.preventDefault()
        this.classList.toggle('div_complate')
        customer=this.dataset.customer
        product=this.dataset.product
        x=this.dataset.ch
        if(x == 'True'){
            action='remove'
        }
        if(x == 'False'){
            action='add'
        }
        management(customer,product,action)
    })
}//end for

for(var i=0 ;i<check.length ;i++){
    x=check[i].dataset.ch
    if(x == 'True'){
        check[i].classList.toggle('div_complate')
    }
}//end for

function management(customer,product,action){
    var url='/product/mangement/'
    fetch(url,{
        method:'POST',
        headers:{'Content-Type':'application/json','X-CSRFToken':csrftoken},
        body:JSON.stringify({'customer':customer,'action':action,'product':product})
    })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        console.log(data)
        window.location.reload()
    })
}