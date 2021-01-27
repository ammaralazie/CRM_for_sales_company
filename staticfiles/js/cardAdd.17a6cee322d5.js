var button=document.getElementsByClassName('add_button')
console.log(button)

for(var i=0 ;i<button.length;i++){
    button[i].addEventListener('click',function(e){
        e.preventDefault()
        var slug=this.dataset.slug
        var action=this.dataset.action
        if(user != 'AnonymousUser'){
            sendCard(slug,action)
        }
    }//function
    )//end event
}//end for


function sendCard(slug,action){

    var url='product/encrement/'
    fetch(url,{
        method:'POST',
        headers:{'Content-Type':'application/json','X-CSRFToken':csrftoken},
        body:JSON.stringify({'slug':slug,'action':action})
    })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        console.log(data)
        window.location.reload()
    })

}//end function