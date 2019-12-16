
function openMobileNav() {
  var navbar = document.getElementById("navbar");
  if (navbar.className === "bg-dark") {
    navbar.className += " responsive";
  } else {
    navbar.className = "bg-dark";
  }
}

document.getElementById("navbar").onclick=function() {
  openMobileNav();
}
