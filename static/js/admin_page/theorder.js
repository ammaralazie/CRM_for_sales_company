var settngs=document.getElementById('setting')
console.log('settings :',settngs)

settngs.addEventListener('click',function(e){
    e.preventDefault()
    var tool_order=document.getElementById('tool_order')
    tool_order.classList.toggle('tool_order_show')
    tool_order.children[0].classList.toggle('showdiv')

})


var order_container=document.getElementById('order_container')
console.log('order_container :',order_container)
var print_order=document.getElementById('print_order')

print_order.addEventListener('click',function(e){
    e.preventDefault()
    document.body.innerHTML=order_container.innerHTML
    window.print()
    window.location.reload()
})
