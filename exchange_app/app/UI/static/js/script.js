document.addEventListener('DOMContentLoaded', function() {
    const productsContainer = document.getElementById('productsContainer');

    fetch('/api/products')
        .then(response => response.json())
        .then(products => {
            products.forEach(product => {
                const productElement = document.createElement('div');
                productElement.innerHTML = `
                    <h2>${product.name}</h2>
                    <p>Price in USD: $${product.price_usd.toFixed(2)}</p>
                    <p>Price in PLN: ${product.price_pln.toFixed(2)} PLN</p>
                `;
                productsContainer.appendChild(productElement);
            });
        })
        .catch(error => console.error('Error loading the products:', error));
});
