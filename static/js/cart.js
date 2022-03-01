var updateBtns = document.getElementsByClassName('update-cart')

// loop through the buttons
for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        // get product id set
        // this represents the item clicked
        var productId = this.dataset.product  
        var action = this.dataset.action
        console.log('productId:',productId,'action:',action)
        console.log('user:',user)
        // check for anonymous user
        if(user==='AnonymousUser'){
            console.log('Not LOgged in')
        }else{
            // calling function
            updateUserOrder(productId,action)
        }

    })
}

function updateUserOrder(productId,action){
    console.log('User is authenticated,sending data...')
    // send data to a view
    var url = '/update_item/'
    // make post request
    // using fetch api
    fetch(url,{
        // send post data
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            // get csrf token
            'X-CSRFToken':csrftoken,
        },
        // send body 
        body:JSON.stringify({'productId':productId,'action':action})
    })
    // return promise
    .then((response) => {
        return response.json();
    })
    .then((data)=>{
        console.log('Data:',data)
        location.reload()
    })


}