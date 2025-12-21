// function showPage(pageId) {
//     const pages = document.querySelectorAll('.page');
//     pages.forEach(page => page.classList.remove('active'));
//     document.getElementById(pageId).classList.add('active');
    
//     const navLinks = document.getElementById('navLinks');
//     navLinks.classList.remove('active');
    
//     window.scrollTo(0, 0);
// }

function toggleMenu() {
    const navLinks = document.getElementById('navLinks');
    navLinks.classList.toggle('active');
}