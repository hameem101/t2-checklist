/* =====================================================

   LOCAL RETAIL WEBSITE - JAVASCRIPT (FastAPI Version)

   This file connects the HTML page to the FastAPI backend

===================================================== */


/* =====================================================

   STEP 1 - SELECT ALL REQUIRED HTML ELEMENTS

   We use document.getElementById() to connect JavaScript

   to elements already created in index.html

===================================================== */

// Customer registration inputs

const emailInput = document.getElementById("email");

const firstNameInput = document.getElementById("firstName");

const lastNameInput = document.getElementById("lastName");

const cityInput = document.getElementById("city");

const countryInput = document.getElementById("country");

// Buttons

const registerBtn = document.getElementById("registerBtn");

const loadProductsBtn = document.getElementById("loadProductsBtn");

const filterBtn = document.getElementById("filterBtn");

// Filter input

const categoryIdInput = document.getElementById("categoryIdInput");

// Product display container

const productContainer = document.getElementById("productContainer");


/* =====================================================

   SECTION A - REGISTER CUSTOMER (POST REQUEST)

===================================================== */

// Add event listener to Register button

registerBtn.addEventListener("click", function () {

    // Create a JavaScript object using input values

    const customerData = {

        email: emailInput.value,

        first_name: firstNameInput.value,

        last_name: lastNameInput.value,

        city: cityInput.value,

        country: countryInput.value

    };

    // Send data to FastAPI backend using fetch

    fetch("http://127.0.0.1:8000/customers", {

        method: "POST",  // We are sending data

        headers: {

            "Content-Type": "application/json" // Tell server we are sending JSON

        },

        body: JSON.stringify(customerData) // Convert JS object to JSON

    })

    .then(response => response.json())  // Convert server response to JSON

    .then(data => {

        alert("Customer registered successfully!");

        // Clear form fields after success

        emailInput.value = "";

        firstNameInput.value = "";

        lastNameInput.value = "";

        cityInput.value = "";

        countryInput.value = "";

    })

    .catch(error => {

        console.error("Error registering customer:", error);

    });

});


/* =====================================================

   SECTION B - LOAD ALL PRODUCTS (GET REQUEST)

===================================================== */

// When user clicks "Load All Products"

loadProductsBtn.addEventListener("click", function () {

    fetch("http://127.0.0.1:8000/products")

        .then(response => response.json()) // Convert response to JSON

        .then(data => {

            displayProducts(data); // Call function to display products

        })

        .catch(error => {

            console.error("Error loading products:", error);

        });

});


/* =====================================================

   SECTION C - FILTER PRODUCTS BY CATEGORY

===================================================== */

filterBtn.addEventListener("click", function () {

    const categoryId = categoryIdInput.value;

    // Build URL with query parameter

    const url = `http://127.0.0.1:8000/products?category_id=${categoryId}`;

    fetch(url)

        .then(response => response.json())

        .then(data => {

            displayProducts(data);

        })

        .catch(error => {

            console.error("Error filtering products:", error);

        });

});


/* =====================================================

   FUNCTION TO DISPLAY PRODUCTS ON THE PAGE

   This function is reused for both load all

   and filtered products

===================================================== */

function displayProducts(products) {

    // Clear previous results

    productContainer.innerHTML = "";

    // Loop through each product in the array

    products.forEach(function (product) {

        // Create a new div for each product

        const productCard = document.createElement("div");

        productCard.classList.add("product-card");

        // Insert product details into HTML

        productCard.innerHTML = `
<strong>${product.product_name}</strong><br>

            Category: ${product.category_name}<br>

            Price: £${product.price}<br>

            Stock: ${product.stock}

        `;

        // Add product card to page

        productContainer.appendChild(productCard);

    });

}
