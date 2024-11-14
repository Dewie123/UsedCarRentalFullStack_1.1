

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


function openReviewModal() {
    document.getElementById("reviewModal").style.display = "block";
}

function closeReviewModal() {
    document.getElementById("reviewModal").style.display = "none";
}

function submitReview(event) {
    event.preventDefault();  // Prevents form from submitting normally

    const rating = document.getElementById("rating").value;
    const review = document.getElementById("review").value;
    const listing_id = document.getElementById("listing_id").value;


    console.log("Rating:", rating);
    console.log("Review:", review);
    console.log("Listing ID:", listing_id);
    
    // Send data to backend using Fetch API
    fetch('/submit_review', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rating, review,listing_id })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Review submitted successfully!");
            closeReviewModal();
        } else {
            alert("Failed to submit review.");
        }
    })
    .catch(error => console.error('Error:', error));
}