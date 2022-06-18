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

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
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