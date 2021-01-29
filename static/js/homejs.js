var main=document.getElementsByClassName('serch__nav')
var search=document.getElementsByClassName('serch')
search[0].addEventListener('click',function(){
    main[0].classList.toggle('show_search')
   console.log( main[0].classList)
}//end function
)//end event listener


var lis_user=document.getElementsByClassName('list_user')
var user_icon=document.getElementsByClassName('user')

user_icon[0].addEventListener('click',function(){

    lis_user[0].classList.toggle('show_list_user')

}//end function
)//end even listener

var bod=document.body
bod.children[0].onscroll=function(){
    this.classList.toggle('show_nav')
}

if(user == 'AnonymousUser' ){
    var mainc=document.getElementsByClassName('container_login')
    mainc[0].classList.toggle('container_show')
    var cover_login=document.getElementsByClassName('container_login')
    cover_login[0].classList.toggle('cover_show')
    var close=document.getElementsByClassName('close_span')
    close[0].classList.toggle('close_show')

    var login=document.getElementsByClassName('login')
    login[0].classList.toggle('show_login')
    
    close[0].addEventListener('click',function(){
       
        console.log( main[0].classList[1])
        mainc[0].classList.remove('container_show')
        cover_login[0].classList.remove('cover_show')
        login[0].classList.remove('show_login')
        close[0].classList.remove('close_show')
    }//end dunction
    )//end event listener
}//end if condation
