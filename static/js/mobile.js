var showmenu=document.getElementsByClassName('nav__options')
var eventspan=document.getElementsByClassName('nav_span')
console.log(showmenu)
console.log(eventspan)
eventspan[0].addEventListener('click',function(){
    showmenu[0].classList.toggle('show___menu')
}//end event
)
