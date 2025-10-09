// GET call
fetch('http://127.0.0.1:8000/api/menu-items')
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })

// POST, PUT and PATCH Calls    
const payload = {
    "title": "Ambrosia Ice cream",
    "price": 5.00,
    "inventory": 100
}
const endpoint1 = 'http://127.0.0.1:8000/api/menu-items'
fetch(endpoint1,
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })

// DELETE calls
const endpoint2 = 'http://127.0.0.1:8000/api/menu-items/17'
fetch(endpoint2,
    {
        method: 'DELETE',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })

// Making authenticated calls with tokens
const endpoint3 = 'http://127.0.0.1:8000/api/menu-items/17'
const token = "Some token"
fetch(endpoint,
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authentication': 'Bearer ' + token
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })

