document.addEventListener('DOMContentLoaded', function () {
    const burgerBtn = document.getElementById('burgerBtn');
    const mobileMenu = document.getElementById('mobileMenu');

    burgerBtn.addEventListener('click', function () {
        mobileMenu.classList.toggle('open');
    });

    const menuLinks = document.querySelectorAll('.mobile-menu-item');
    menuLinks.forEach(link => {
        link.addEventListener('click', function () {
            mobileMenu.classList.remove('open');
        });
    });

    document.addEventListener('click', function (event) {
        if (!mobileMenu.contains(event.target) && !burgerBtn.contains(event.target)) {
            mobileMenu.classList.remove('open');
        }
    });
})