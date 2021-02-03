
var event_optint=document.getElementsByClassName('optint_page')

for(var i=0 ;i<event_optint.length;i++){
    console.log('o')
event_optint[i].addEventListener('click',function(e){
    e.preventDefault()
    this.children[0].checked="checked"
    var form_option=document.getElementById('submit')
    form_option.submit()
})
}
