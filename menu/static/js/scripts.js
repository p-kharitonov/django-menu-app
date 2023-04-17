var toggler = document.getElementsByClassName("menu_caret");
var i;

for (i = 0; i < toggler.length; i++) {
    toggler[i].addEventListener("click", function () {
        this.parentElement.querySelector(".menu_item__nested").classList.toggle("menu_item__active");
        this.classList.toggle("menu_caret__down");
    });
} 