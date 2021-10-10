const navLinks = document.querySelectorAll('.nav-link')
navLinks.forEach(link => {
  if (link.href == document.URL) {
    link.classList.add("active")
    if (link.classList.contains("dropdown-item")){
      link.parentElement.parentElement.classList.add("show-dropdown-container");
    }

  } else {
    link.classList.remove("active")
    // link.parentElement.parentElement.classList.remove("show-dropdown-container");
  }
})


const dropdown = document.querySelectorAll(".dropdown-btn");
for (let i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function () {
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.classList.contains("show-dropdown-container")) {
      dropdownContent.classList.remove( "show-dropdown-container");
    } else {
      dropdownContent.classList.add("show-dropdown-container");
    }
  });
}


$(document).ready(function () {
  // console.log('data-table');
  $(window).scroll(function () {
    if ($(window).scrollTop() + $(window).height() > $(document).height() - 5) {
      $(".aside-container").css("bottom", $(".footer").outerHeight()+2)
      $(".aside-container").addClass("small-aside")
      $(".footer").removeClass("footer-shrink")
    } else {
      $(".aside-container").css("bottom", "0")
      $(".aside-container").removeClass("small-aside")
      $(".footer").addClass("footer-shrink")
    }
  });
});

const deleteBtn = document.querySelectorAll(".trash, .dlt")

deleteBtn.forEach(btn=>{
    btn.addEventListener("click",()=>{
        btn.parentElement.parentElement.style.display = "none"
    })
})


const hamburger = document.querySelector(".hamburger")
const sideBarClose = document.querySelector(".sideBarClose")
const aside = document.querySelector(".aside-container")

hamburger.addEventListener("click", ()=>{
  aside.classList.toggle("show-aside")
})

sideBarClose.addEventListener("click", ()=>{
  aside.classList.remove("show-aside")
})

const fileFields = document.querySelectorAll(".form-control-file")
window.addEventListener("load", ()=>{
  fileFields.forEach(item=>{
    item.classList.add("form-control")
  })
})