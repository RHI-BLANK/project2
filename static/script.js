// Smooth Scrolling for Navigation Links
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Form Validation for the Contact Form
document.getElementById('contact-form').addEventListener('submit', function(e) {
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    let valid = true;

    if (!name) {
        valid = false;
        alert('Please enter your name.');
    }
    if (!email) {
        valid = false;
        alert('Please enter your email.');
    }
    if (!message) {
        valid = false;
        alert('Please enter your message.');
    }

    if (!valid) {
        e.preventDefault();
    }
});

// Interactive Animations for Elements
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
        } else {
            entry.target.classList.remove('animate');
        }
    });
});

document.querySelectorAll('.animate-on-scroll').forEach(el => {
    observer.observe(el);
});
