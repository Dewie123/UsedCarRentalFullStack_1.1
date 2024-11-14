const carouselContainer = document.querySelector('.carousel-container');
const carListings = document.querySelectorAll('.car-listing-star');
let currentIndex = 0;

function updateCarousel() {
    const totalListings = carListings.length;
    // Move the carousel container
    const offset = -currentIndex * 100; // -100% for each listing
    carouselContainer.style.transform = `translateX(${offset}%)`;
}

// Automatically rotate every 3 seconds
setInterval(() => {
    currentIndex = (currentIndex + 1) % carListings.length; // Increment index and wrap around
    updateCarousel();
}, 3000);



function toggleDropdown() {
    const dropdown = document.getElementById("shortlistedDropdown");
    
    // Toggle the "show" class to display/hide the dropdown
    dropdown.classList.toggle("show");
    
    // Fetch shortlisted items only when the dropdown is opened
    if (dropdown.classList.contains("show")) {
        console.log("Dropdown opened, fetching shortlisted listings...");
        fetchShortlistedListings();
    }
}

async function fetchShortlistedListings() {
    console.log("Fetching shortlisted listings..."); // Debugging statement
    const response = await fetch("/get_shortlisted_listings");
    
    if (response.ok) {
        const listings = await response.json();
        
        const itemsContainer = document.getElementById("shortlistedItems");
        itemsContainer.innerHTML = "";  // Clear any previous items
        
        if (listings.length > 0) {
            listings.forEach(listing => {
                const item = document.createElement("div");
                item.innerHTML = `
                    <a href="/view_listing/${listing.id}">
                        <img src="/${listing.image_path}"  style="width:50px;height:50px;">
                        
                        <p>${listing.carName}</p>
                        <p>Price: ${listing.price}</p>
                    </a>
                `;
                itemsContainer.appendChild(item);
            });
        } else {
            itemsContainer.innerHTML = "<p>No items saved</p>";
        }
    } else {
        console.error("Failed to fetch shortlisted listings");
    }
}

// Close dropdown if clicked outside
window.onclick = function(event) {
    if (!event.target.matches('#shortlistedCartBtn')) {
        const dropdown = document.getElementById("shortlistedDropdown");
        if (dropdown.classList.contains("show")) {
            dropdown.classList.remove("show");
        }
    }
}
