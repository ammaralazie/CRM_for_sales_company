console.log('filte is working ...')

var admin_date=document.getElementById('admin_date')
var date_cover=document.getElementById('date_cover')



admin_date.addEventListener('click', function(e){
    e.preventDefault()
    console.log('filte is working ...')
    date_cover.classList.toggle('show_date_cover')
    console.log(date_cover.classList)

}//end function
)//end event



