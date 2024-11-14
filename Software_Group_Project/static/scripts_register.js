document.getElementById('dealership-option').addEventListener('click', function() {
    document.getElementById('dealership-details').classList.remove('hidden');
});

document.getElementById('no-dealership-option').addEventListener('click', function() {
    document.getElementById('dealership-details').classList.add('hidden');
});


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