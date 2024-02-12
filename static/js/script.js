const hamburgerMenu = () => {
    let iconLinks = document.getElementById('icon-links')
    let nav = document.getElementById('nav')
    let userMessage = document.getElementById('user-message')
    let authIcon = document.getElementById('auth-icon')

    if (iconLinks.style.display === "block") {
        iconLinks.style.display = "none"
        nav.style.display = "flex"
        userMessage.style.display = "block"
        authIcon.style.display = "block"
    } else {
        iconLinks.style.display = "block"
        nav.style.display = "block"
        userMessage.style.display = "none"
        authIcon.style.display = "none"
    }
}