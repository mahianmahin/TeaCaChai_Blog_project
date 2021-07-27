document.getElementById("toggler_id").addEventListener('click', () => {
    document.getElementById("phoneNav").classList.toggle("show");
});

window.addEventListener('scroll', () => {
    var scrolled = window.scrollY;
    
    if (scrolled >= 1) {
        document.getElementById("sticky").classList.add("sticky");
        document.getElementById("phoneNav").classList.add("sticky");
    } else {
        document.getElementById("sticky").classList.remove("sticky");
        document.getElementById("phoneNav").classList.remove("sticky");
    }
});