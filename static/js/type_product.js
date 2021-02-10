var product_type=document.getElementById('Products_Type')
product_type.addEventListener('click',function(e){
    e.preventDefault()
    var show_lis_products=document.getElementById('product_type_list')
    show_lis_products.classList.toggle('show_product_type_list')
})