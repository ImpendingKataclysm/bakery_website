const nav = document.getElementById("main_nav");
const side_nav = document.getElementById("side_nav")
const nav_btn = document.getElementById("nav-btn");
const side_nav_btn = document.getElementById("side_nav_btn");
const side_nav_items = document.getElementsByClassName("sidenav-item");

nav_btn.addEventListener("click", showNav);

if(side_nav_btn)
{
    side_nav_btn.addEventListener("click", showSideNav);
}

if(side_nav_items)
{
    Array.from(side_nav_items).forEach(function (e)
    {
        e.addEventListener("click", showSideNav)
    })
}

function showNav()
{
    nav.classList.toggle("show");
}

function showSideNav()
{
    side_nav.classList.toggle("show");

    if(side_nav_btn.textContent.includes('See'))
    {
        side_nav_btn.textContent = 'Hide Categories';
    }
    else if(side_nav_btn.textContent.includes('Hide'))
    {
        side_nav_btn.textContent = 'See Categories';
    }
}