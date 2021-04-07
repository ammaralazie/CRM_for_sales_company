var scalCursor=document.getElementById('courser')
var image_product=document.getElementById('image_product')
absolute_cursor=document.getElementById('absolute_cursor')
var b=document.body
console.log('working ---')
window.addEventListener('mousemove',cursor)
function cursor(e){
    scalCursor.style.top=e.pageY+"px"
    scalCursor.style.left=e.pageX+"px"
    absolute_cursor.style.top=e.pageY+"px"
    absolute_cursor.style.left=e.pageX+"px"

    image_product.addEventListener('mouseover',function(){
        scalCursor.style.zIndex=1  
        scalCursor.style.visibility='visible'
        b.style.cursor='none'
        absolute_cursor.style.zIndex=1
        absolute_cursor.style.visibility='visible'
    })
    image_product.addEventListener('mouseleave',function(){
        scalCursor.style.zIndex=-4 
        scalCursor.style.visibility='hidden'
        b.style.cursor='auto'
        absolute_cursor.style.zIndex=-4
        absolute_cursor.style.visibility='hidden'
        

    })

}

