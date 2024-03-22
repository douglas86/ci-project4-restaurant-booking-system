/*
This function is to hide and un hide elements when hamburger icon is open or close,
It will also hide the hamburger menu when on a screen tablet or bigger
 */
const hamburgerMenu = () => {
    let iconLinks = document.getElementsByClassName('icon-links')[0]
    let userMessage = document.getElementsByClassName('user-message')[0]
    let authIcon = document.getElementsByClassName('auth-icon')[0]
    let mobile = document.getElementsByClassName('mobile')[0]

    // toggle to show and hide a menu
    if (iconLinks.style.display === "block") {
        iconLinks.style.display = "none"
        userMessage.style.display = 'block'
        authIcon.style.display = 'block'
        mobile.style.display = 'flex'
    } else {
        iconLinks.style.display = "block"
        userMessage.style.display = 'none'
        authIcon.style.display = 'none'
        mobile.style.display = 'block'
    }
}

/*
This function is used to detect screen sizes
 */
const resizeHandler = () => {
    // variable to check window width
    const matchResults = window.matchMedia("(min-width:768px)")

    const mobile = document.getElementsByClassName('mobile')[0]
    const tablet = document.getElementsByClassName('tablet')[0]
    const iconLinks = document.getElementsByClassName('icon-links')[0]

    // when window width is tablet or bigger
    if (matchResults.matches === true) {
        mobile.style.display = 'none'
        tablet.style.display = 'flex'
    } else {
        tablet.style.display = 'none'
        // toggle to change the display of mobile
        // depending on if the style for iconLinks variable is block or not
        if (iconLinks.style.display === 'block') {
            mobile.style.display = 'block'
        } else {
            mobile.style.display = 'flex'
        }
    }
}

// event listener for handling the width resizing
window.addEventListener('resize', resizeHandler)


setTimeout(() => {
    let message = document.getElementById("message_container")

    if (!TypeError) {
        message.style.display = 'none'
    }

}, 5000)


