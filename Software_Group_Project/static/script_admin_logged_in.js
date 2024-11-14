//manage users

document.addEventListener('DOMContentLoaded', function () {
    // Get the search input and table rows
    const searchInput = document.getElementById('user-search');
    const tableBody = document.querySelector('#manage-users tbody');
    const tableRows = tableBody.getElementsByTagName('tr');

    // Add event listener for input in the search bar
    searchInput.addEventListener('input', function () {
        const searchTerm = searchInput.value.toLowerCase(); // Convert search term to lowercase

        // Loop through all the rows in the table
        Array.from(tableRows).forEach(row => {
            const usernameCell = row.cells[2]; // The third column (index 2) contains the username
            const username = usernameCell ? usernameCell.textContent.toLowerCase() : ''; // Get the username

            if (username.includes(searchTerm)) {
                row.style.display = ''; // Show row if the username matches
                row.classList.add('selected'); // Highlight the row
            } else {
                row.style.display = 'none'; // Hide row if the username doesn't match
                row.classList.remove('selected'); // Remove highlight
            }
        });
    });

    // Handle Edit button click
    Array.from(document.querySelectorAll('.edit-btn')).forEach(button => {
        button.addEventListener('click', function () {

            const field = cell.getAttribute('data-field');
            
            if(field !== 'status'){

            const row = button.closest('tr');
            const saveButton = row.querySelector('.save-btn');
            const editButton = row.querySelector('.edit-btn');
            
            // Toggle visibility of buttons
            editButton.style.display = 'none';
            saveButton.style.display = '';

            // Make cells editable by converting them to input fields
            row.querySelectorAll('.editable').forEach(cell => {

                
                
                
                    const cellValue = cell.textContent;
                    cell.innerHTML = `<input type="text" value="${cellValue}" class="input-field">`;

                
                
            });
            }

            
        });
    });

    // Handle Save button click
    Array.from(document.querySelectorAll('.save-btn')).forEach(button => {
        button.addEventListener('click', function () {
            const row = button.closest('tr');
            const userId = row.querySelector('[data-field="user_id"] input').value;
    
            // Collect the updated values from the input fields
            const updatedData = {
                user_id: userId,
                username: row.querySelector('[data-field="username"] input').value,
                password: row.querySelector('[data-field="password"] input').value,
                email: row.querySelector('[data-field="email"] input').value,
                name: row.querySelector('[data-field="name"] input').value,
                description: row.querySelector('[data-field="description"] input').value,
                phone_number: row.querySelector('[data-field="phone_number"] input').value,
                user_type: row.querySelector('[data-field="user_type"] input').value
            };
    
            console.log("Sending data to backend:", updatedData);  // Debugging line
    
            // Send updated data to the backend (via an AJAX call)
            fetch('/update_user', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(updatedData)
            })
            .then(response => response.json())
            .then(data => {
                console.log("Backend response:", data);
                // Check for success and update the row if necessary
                if (data.success) {
                    row.querySelectorAll('.editable').forEach(cell => {
                        const field = cell.getAttribute('data-field');
                        const inputField = cell.querySelector('input');
                        if (inputField) {
                            cell.innerHTML = inputField.value;
                        }
                    });
    
                    // Toggle buttons back to "Edit"
                    button.style.display = 'none';
                    row.querySelector('.edit-btn').style.display = '';
                } else {
                   
                }
            })
            .catch(error => {
                console.error('Error in saving:', error);  // Log fetch error
                
            });
        });
    });
});


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


document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.querySelectorAll('.edit-btn');
    
    editButtons.forEach(button => {
        button.addEventListener('click', function () {
            const row = button.closest('tr'); // Get the closest row (tr)
            const cells = row.querySelectorAll('.editable');
            
            // Toggle the row between editable form and regular view
            cells.forEach(cell => {
                const field = cell.dataset.field;
                const value = cell.textContent.trim();
                
                // Replace the cell content with an input field prefilled with the existing value
                const input = document.createElement('input');
                input.type = 'text';
                input.value = value;
                input.classList.add('form-control'); // Optional: add a class for styling

                // Add input field to the cell, replacing the text content
                cell.innerHTML = ''; // Clear the current cell content
                cell.appendChild(input);
            });

            // Hide the Edit button and show the Save button
            row.querySelector('.edit-btn').style.display = 'none';
            row.querySelector('.save-btn').style.display = 'inline-block';
        });
    });

    const saveButtons = document.querySelectorAll('.save-btn');
    saveButtons.forEach(button => {
        button.addEventListener('click', function () {
            const row = button.closest('tr');
            const cells = row.querySelectorAll('.editable');

            // Collect the updated values
            const updatedData = {};
            cells.forEach(cell => {
                const field = cell.dataset.field;
                updatedData[field] = cell.querySelector('input').value;
            });

            // Here, you can send `updatedData` to your backend to update the user data
            // Use AJAX or a form submission to update the database
            console.log(updatedData);

            // Update the row with the new values
            cells.forEach(cell => {
                const inputValue = cell.querySelector('input').value;
                cell.innerHTML = inputValue; // Set the text content back to the cell
            });

            // Hide the Save button and show the Edit button
            row.querySelector('.save-btn').style.display = 'none';
            row.querySelector('.edit-btn').style.display = 'inline-block';
        });
    });
});


document.addEventListener('DOMContentLoaded', function () {
    // Handle Deactivate button click
    Array.from(document.querySelectorAll('.deactivate-btn')).forEach(button => {
        button.addEventListener('click', function () {
            const row = button.closest('tr');
            const userId = row.querySelector('[data-field="user_id"]').textContent;

            // Show confirmation dialog
            const confirmDeactivation = confirm("Are you sure you want to deactivate this user?");
            
            if (confirmDeactivation) {
                // Send a request to deactivate the user
                fetch('/deactivate_user', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ user_id: userId })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert(data.message); // Show success message
                        
                        // Update the row to reflect the deactivated status
                        const statusCell = row.querySelector('[data-field="status"]');
                        
                        if (statusCell) {
                            statusCell.textContent = 'Inactive'; // Update status cell
                            statusCell.classList.add('inactive'); // Optionally add a class for styling
                        } else {
                            console.error("Status cell not found in row");
                        }

                        // Optionally disable the deactivate button or change its text
                        button.disabled = true;
                        button.textContent = 'Deactivated';
                    } else {
                        alert(data.message); // Show failure message
                    }
                })
                .catch(error => {
                    console.error('Error in deactivating user:', error);
                    alert('Error deactivating user: ' + error.message);
                });
            }
        });
    });
});




    // Show modal when "Add User Type" button is clicked
    document.getElementById('add-user-type-btn').addEventListener('click', function () {
        document.getElementById('add-user-type-modal').style.display = 'block';
    });

    // Close modal
    function closeModal() {
        document.getElementById('add-user-type-modal').style.display = 'none';
    }

    // Handle form submission
    document.getElementById('add-user-type-form').addEventListener('submit', function (event) {
        event.preventDefault();

        const userTypeData = {
            user_type: document.getElementById('user_type').value,
            user_type_name: document.getElementById('user_type_name').value,
            create_listing: document.getElementById('create_listing').checked ? 'Yes' : 'No',
            delete_listing: document.getElementById('delete_listing').checked ? 'Yes' : 'No',
            update_listing: document.getElementById('update_listing').checked ? 'Yes' : 'No',
            view_listing: document.getElementById('view_listing').checked ? 'Yes' : 'No',
        };

        // Send data to backend using AJAX
        fetch('/add_user_type', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userTypeData),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('User Type added successfully');
                location.reload();  // Reload page to show updated data
            } else {
                alert('Failed to add User Type');
            }
        })
        .catch(error => console.error('Error:', error));
        
        closeModal(); // Close modal after submission
    });


    document.getElementById('user-id-search').addEventListener('input', function () {
        const userIdValue = this.value.toLowerCase();
        const rows = document.querySelectorAll('#manage-users tbody tr');

        rows.forEach(row => {
            const userId = row.querySelector('[data-field="user_type"]').innerText.toLowerCase();
            row.style.display = userId.includes(userIdValue) ? '' : 'none';
        });
    });

    document.getElementById('bulk-deactivate-btn').addEventListener('click', async function () {
        const userTypeToDeactivate = document.getElementById('bulk-deactivate-user-type').value.trim();
    
        if (userTypeToDeactivate === "") {
            alert("Please enter a user type to deactivate.");
            return;
        }
    
        try {
            const response = await fetch('/deactivate_users_by_type', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ user_type: userTypeToDeactivate })
            });
            const result = await response.json();
    
            if (result.success) {
                alert(result.message);
                // Optionally refresh the page or update the table to reflect changes
            } else {
                alert("Error: " + result.message);
            }
        } catch (error) {
            console.error("Error deactivating users:", error);
            alert("An error occurred while deactivating users.");
        }
    });



    // Add event listeners for the Edit and Save buttons
document.querySelectorAll('.edit-btn').forEach(button => {
    button.addEventListener('click', function () {
        const row = this.closest('tr');
        
        // Make the cells editable
        row.querySelectorAll('.editable1').forEach(cell => {
            const field = cell.getAttribute('data-field');
            const value = cell.textContent.trim();
            cell.innerHTML = `<input type="text" value="${value}" data-field="${field}">`;
        });
        
        // Hide the edit button and show the save button
        row.querySelector('.edit-btn').style.display = 'none';
        row.querySelector('.save-btn').style.display = 'inline-block';
    });
});

document.querySelectorAll('.save-btn').forEach(button => {
    button.addEventListener('click', async function () {
        const row = this.closest('tr');
        const id = row.getAttribute('data-id');
        const updatedData = {};

        // Collect updated values from input fields
        row.querySelectorAll('input').forEach(input => {
            updatedData[input.getAttribute('data-field')] = input.value.trim();
        });

        // Send the updated data to the server
        try {
            const response = await fetch('/update_user_type_permission', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ id, ...updatedData }),
            });
            const result = await response.json();

            if (result.success) {
                // Update the table with the new values
                row.querySelectorAll('.editable').forEach(cell => {
                    const field = cell.getAttribute('data-field');
                    const newValue = updatedData[field];
                    cell.textContent = newValue;
                });
                alert('Permissions updated successfully.');
            } else {
                alert('Failed to update permissions.');
            }
        } catch (error) {
            console.error("Error updating permissions:", error);
            alert('An error occurred while updating permissions.');
        }

        // Hide the save button and show the edit button again
        row.querySelector('.edit-btn').style.display = 'inline-block';
        row.querySelector('.save-btn').style.display = 'none';
    });
});