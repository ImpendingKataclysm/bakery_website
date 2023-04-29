const nav = document.querySelector("nav");
const nav_btn = document.getElementById("nav-btn");

nav_btn.addEventListener("click", showNav);

function showNav()
{
    nav.classList.toggle("show");
}