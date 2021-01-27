console.log('working search ...')
var search_d=document.getElementById('Date')
var search_s=document.getElementById('State')
var search_o=document.getElementById('Order')

var form_date=document.getElementById('form_date')
var form_state=document.getElementById('state_form')
var order_form=document.getElementById('order_form')

search_d.addEventListener('click',function(e,d=form_date,s=form_state,o=order_form){
    e.preventDefault()
    d.classList.toggle('show_form_date')
    s.classList.remove('show_state_form')
    o.classList.remove('show_order_form')
})

search_o.addEventListener('click',function(e,d=form_date,s=form_state,o=order_form){
    e.preventDefault()
    o.classList.toggle('show_order_form')
    s.classList.remove('show_state_form')
    d.classList.remove('show_form_date')

})

search_s.addEventListener('click',function(e,d=form_date,s=form_state,o=order_form){
    e.preventDefault()
    s.classList.toggle('show_state_form')
    d.classList.remove('show_form_date')
    o.classList.remove('show_order_form')
})

