var stripe = Stripe('pk_test_51OUXtVAkBLVhTvf1vV0EQeDQnzXFENifuC3ip4YLdTn16CjZEPsygAJ2qGeZcgc6jMEwYL7NRLA5L5iGT9B9AJQ600Si88V3Jp');

var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();

    fetch('http://127.0.0.1:8000/stripe/session', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            data: [
                { price: 'price_1Q4qRGAkBLVhTvf15SNrvLRS', quantity: 1 }
            ]
        }),
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(session) {
        return stripe.redirectToCheckout({ sessionId: session.session_id });
    })
    .then(function(result) {
        if (result.error) {
            // Exibir erro ao cliente
            console.error(result.error.message);
        }
    })
    .catch(function(error) {
        console.error('Error:', error);
        alert('Something went wrong: ' + error.message);
    });
});