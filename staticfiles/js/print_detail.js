console.log('print working ...')
if(complate == 'complate'){
var eventPrint=document.getElementById('print_detail')
var allwindow=document.body
var printWindow=document.getElementById('alldetail')


eventPrint.addEventListener('click',function(e){
    e.preventDefault()
    var cover=document.getElementById('cover')
    
    for (var i=0 ;i<cover.children.length;i++){
        x= cover.children[i].querySelectorAll('div')
        for(j=0 ;j<x.length;j++){
            x[j].style.color="#000"
        }
        cover.children[i].querySelector('label').classList.toggle('heddin_background')
    }
    allwindow.innerHTML=printWindow.innerHTML
    window.print()
    window.location.reload()
})
}//end if