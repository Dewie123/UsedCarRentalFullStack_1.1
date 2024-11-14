function previewImages() {
    const preview = document.getElementById('imagePreview');
    const files = document.getElementById('images').files;

    preview.innerHTML = '';  // Clear previous previews

    if (files.length > 0) {
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            const reader = new FileReader();

            reader.onload = function (e) {
                const img = document.createElement('img');
                img.src = e.target.result;
                img.style.width = '100px';  // Set a fixed width for previews
                img.style.margin = '5px';    // Add some space between images
                preview.appendChild(img);
            }

            reader.readAsDataURL(file);  // Convert the file to a Data URL
        }
    }
}

function selectListingType(type) {
    console.log(`Selected Listing Type: ${type}`);

    document.getElementById('listing_type').value = type; 
    // You can add any additional logic you need here based on the selected type
    // For example, you might want to highlight the selected button
    const buttons = document.querySelectorAll('.listing-btn');
    
    buttons.forEach(button => {
        button.classList.remove('selected');  // Remove the selected class from all buttons
    });
    
    const selectedButton = document.getElementById(`${type}_listing`);
    selectedButton.classList.add('selected');  // Highlight the selected button
}