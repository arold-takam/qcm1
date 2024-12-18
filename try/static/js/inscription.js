document.addEventListener("DOMContentLoaded", () => {
    let menubutton = document.getElementById("mnu");
    let menu=document.getElementById("setting");
    let closeMenu=document.getElementById("cls");


  menubutton.addEventListener("click", () => {
      menu.style.position="fixed";
      menu.style.left="0";
  });

  closeMenu.addEventListener("click", () => {
      menu.style.left="-50rem";
  })
});
