// Form and loading screen fader
const form = document.getElementById('Form');
const loadingText = document.getElementById('loadingText');

if(form && loadingText) {
    form.addEventListener('submit', (e) => {
    // e.preventDefault();
    form.classList.toggle('fade-out');
    loadingText.classList.toggle('hide');
    loadingText.classList.toggle('transparent');
    // loadingText.classList.toggle('show');
    loadingText.classList.toggle('fade-in');
    });
}

