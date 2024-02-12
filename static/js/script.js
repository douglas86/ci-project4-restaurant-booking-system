const hamburgerMenu = () => {
    let x = document.getElementById('icon-links')

    if (x.style.display === "block") {
        x.style.display = "none"
    } else {
        x.style.display = "block"
    }
}