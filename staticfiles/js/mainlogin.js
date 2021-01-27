var show=document.getElementsByClassName('fa-eye')
console.log(show)
check=true
password=document.querySelectorAll('[type="password"]');
show[0].onclick=function(){
    if(check == true){
        password[0].type="text"
        check=false
    }
    else{
        password[0].type="password" 
        check=true
    }
    
}