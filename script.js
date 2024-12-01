let slideIndex = 0;
showSlides();

function plusSlides(n) {
    slideIndex += n;
    showSlides();
}

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("slide");
    if (slideIndex >= slides.length) { slideIndex = 0; }
    if (slideIndex < 0) { slideIndex = slides.length - 1; }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slides[slideIndex].style.display = "block";  
}

setInterval(() => {
    slideIndex++;
    showSlides();
}, 3000); // Change image every 3 seconds

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('reservation-form');
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', (event) => {
        let isValid = true;
        let errors = [];

        // Validate Full Name
        const name = form.elements['name'].value.trim();
        if (name === '') {
            isValid = false;
            errors.push('Full Name is required.');
        }

        // Validate Email
        const email = form.elements['email'].value.trim();
        if (!validateEmail(email)) {
            isValid = false;
            errors.push('Invalid email address.');
        }

        // Validate Phone Number
        const phone = form.elements['phone'].value.trim();
        if (phone === '') {
            isValid = false;
            errors.push('Phone Number is required.');
        }

        // Validate Date
        const date = form.elements['date'].value;
        if (date === '') {
            isValid = false;
            errors.push('Reservation Date is required.');
        }

        // Validate Time
        const time = form.elements['time'].value;
        if (time === '') {
            isValid = false;
            errors.push('Reservation Time is required.');
        }

        // Validate Number of Guests
        const guests = form.elements['guests'].value;
        if (guests < 1 || guests > 20) {
            isValid = false;
            errors.push('Number of Guests must be between 1 and 20.');
        }

        if (!isValid) {
            event.preventDefault(); // Prevent form submission
            errorMessage.innerHTML = errors.join('<br>');
            errorMessage.style.display = 'block';
        } else {
            errorMessage.style.display = 'none';
        }
    });

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
});
document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.interactive-image');
    
    images.forEach(image => {
        image.addEventListener('click', () => {
            alert(`You clicked on ${image.alt}`);
        });
    });
});
