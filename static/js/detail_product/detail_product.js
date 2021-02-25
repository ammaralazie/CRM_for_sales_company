console.log('working ...')

detail_description=document.getElementById('detail_description')

console.log(detail_description)
detail_description.addEventListener('click',function(e){
    e.preventDefault()
    this.classList.toggle('increse_height')
})


plus=document.getElementById('plus')

plus.addEventListener('click',function(e){
    e.preventDefault()
    id_qunatity=document.getElementById('id_qunatity')
    val=parseInt(id_qunatity.textContent)
    val=val+1
    id_qunatity.textContent=val
})

munes=document.getElementById('munes')

munes.addEventListener('click',function(e){
    e.preventDefault()
    id_qunatity=document.getElementById('id_qunatity')
    val=parseInt(id_qunatity.textContent)
    if (val != 0){val=val-1}
    
    id_qunatity.textContent=val
})