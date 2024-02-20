/*
This function is to hide and un hide elements when hamburger icon is open or close,
It will also hide the hamburger menu when on a screen tablet or bigger
 */
const hamburgerMenu = () => {
	let iconLinks = document.getElementById("icon-links");
	let nav = document.getElementById("nav");
	let userMessage = document.getElementById("user-message");
	let authIcon = document.getElementsByClassName("auth-icon")[0];

	if (iconLinks.style.display === "block") {
		iconLinks.style.display = "none";
		nav.style.display = "flex";
		userMessage.style.display = "block";
		authIcon.style.display = "block";
	} else {
		iconLinks.style.display = "block";
		nav.style.display = "block";
		userMessage.style.display = "none";
		authIcon.style.display = "none";
	}
};

const dropdownMenu = () => {
	document.getElementById("dropdownContent").classList.toggle("show");
};

// Close dropdown menu if user clicks outside
window.onclick = (event) => {
	if (!event.target.matches(".dropdownButton")) {
		let dropdown = document.getElementsByClassName("dropdownContent");

		for (let i = 0; i < dropdown.length; i++) {
			let openDropdown = dropdown[i];
			if (openDropdown.classList.contains("show")) {
				openDropdown.classList.remove("show");
			}
		}
	}
};
