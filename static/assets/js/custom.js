$( document ).ready(function() {
    // const swiper = new Swiper('.swiper', {
    //     // Optional parameters
    //     direction: 'horizontal',
    //     loop: true,

    //     // If we need pagination
    //     pagination: {
    //     el: '.swiper-pagination',
    //     },

    //     // Navigation arrows
    //     navigation: {
    //     nextEl: '.swiper-button-next',
    //     prevEl: '.swiper-button-prev',
    //     },

    //     // And if we need scrollbar
    //     // scrollbar: {
    //     //   el: '.swiper-scrollbar',
    //     // },
    // });

    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

    var quill = new Quill('#editor', {
        theme: 'snow'
    });

});

var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;
function myFunction() {
if (window.pageYOffset > sticky) {
    navbar.classList.add("sticky") // para que se vea el navbar cuando se desplaza el scroll
    $(".nk-navbar").css('background-color', '#000000f0') // para que se oscurezca el navbar cuando se desplaza el scroll
    mybutton.style.display = "block"; // para que se vea el boton cuando se desplaza el scroll
} else {
    navbar.classList.remove("sticky");
    $(".nk-navbar").css('background-color', '#00000099')
    mybutton.style.display = "none";
}
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

function Copy() {
    let url = document.location.href

    navigator.clipboard.writeText(url)
}