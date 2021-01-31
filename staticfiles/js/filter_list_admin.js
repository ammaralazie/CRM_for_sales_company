console.log('filte is working ...')

var admin_date=document.getElementById('admin_date')
var date_cover=document.getElementById('date_cover')



admin_date.addEventListener('click', function(e){
    e.preventDefault()
    date_cover.classList.toggle('show_date_cover')

}//end function
)//end event



