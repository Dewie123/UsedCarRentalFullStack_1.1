
document.addEventListener('DOMContentLoaded', function () {
    // Get the search input and table rows for car listings
    const searchInput = document.getElementById('listing-search');
    const tableBody = document.querySelector('#manage-listings tbody');  // Target the tbody specifically
    const tableRows = tableBody.getElementsByTagName('tr'); // Get all rows in the table body

    // Add event listener for input in the search bar
    searchInput.addEventListener('input', function () {
        const searchTerm = searchInput.value.toLowerCase(); // Convert search term to lowercase

        // Loop through all the rows in the table
        Array.from(tableRows).forEach(row => {
            const carNameCell = row.cells[2]; // The third column (index 2) contains the car name
            const carName = carNameCell ? carNameCell.textContent.toLowerCase() : ''; // Get the car name

            if (carName.includes(searchTerm)) {
                row.style.display = ''; // Show row if the car name matches
                row.classList.add('selected'); // Highlight the row
            } else {
                row.style.display = 'none'; // Hide row if the car name doesn't match
                row.classList.remove('selected'); // Remove highlight
            }
        });
    });
});
