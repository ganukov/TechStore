const updateBtns = document.getElementsByClassName('update-cart')


for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        const product_id = this.dataset.product
        const action = this.dataset.action

        if (user === 'AnonymousUser') {
        } else {
            updateUserOrder(product_id, action)
        }
    })
}

function updateUserOrder(product_id, action) {

    const url = 'http://www.tech-store.org.uk/cart/update-item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'product_id': product_id, 'action': action})
    })

        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data', data)
            location.reload()
        })
}