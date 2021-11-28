// NAVBAR

const navsubmenus = document.getElementsByClassName('submenu');
const navsubmenusLenght = navsubmenus.length;

function toggleNavSubmenu(submenuId){
    let element = document.getElementById(submenuId);
    if(element.classList.contains('nav-submenu-visible')) {
        closeNavSubmenu(submenuId)
    }
    else{
        openNavSubmenu(submenuId)
    }
}

function openNavSubmenu(submenuId){
    let element = document.getElementById(submenuId);
    let arrow = document.getElementById(submenuId + "-arrow")
    element.classList.add('nav-submenu-visible');
    arrow.classList.replace("fa-angle-down","fa-angle-up");

    for(var i = 0; i < navsubmenusLenght; i++){
        if(navsubmenus[i].id!==submenuId && navsubmenus[i].classList.contains('nav-submenu-visible')){
            navsubmenus[i].classList.remove('nav-submenu-visible');
            submenuarrow = document.getElementById(navsubmenus[i].id + "-arrow")
            submenuarrow.classList.replace("fa-angle-up","fa-angle-down");
        }
    }
}

function closeNavSubmenu(submenuId){
    let element = document.getElementById(submenuId);
    let arrow = document.getElementById(submenuId + "-arrow")
    element.classList.remove('nav-submenu-visible');
    arrow.classList.replace("fa-angle-up","fa-angle-down");
}

function closeNavSubmenuOnOutsideClick(e){ 
    for(var i = 0; i < navsubmenusLenght; i++){
        arrowid = navsubmenus[i].id + "-arrow";
        if(e.target.id !== arrowid && navsubmenus[i].classList.contains('nav-submenu-visible')){
            navsubmenus[i].classList.remove('nav-submenu-visible');
            submenuarrow = document.getElementById(arrowid)
            submenuarrow.classList.replace("fa-angle-up","fa-angle-down");
        }
    }
}
document.addEventListener("click",closeNavSubmenuOnOutsideClick)

// SIDEBAR

function openSidebar(){
    let element = document.getElementById('sidebar');
    element.classList.add('sidebar-show');
}

function closeSidebar(){
    let element = document.getElementById('sidebar');
    element.classList.remove('sidebar-show');
}

function toggleSideBarSubmenu(submenuId){
    let element = document.getElementById(submenuId);
    let arrow = document.getElementById(submenuId + "-plus")
    if(element.classList.contains('sidebar-submenu-show')) {
        element.classList.remove('sidebar-submenu-show');
        arrow.classList.replace("fa-minus-square","fa-plus-square")  
    }
    else{
        element.classList.add('sidebar-submenu-show');
        arrow.classList.replace("fa-plus-square","fa-minus-square")
    }
    
}

// ACTIVE PAGE
let mainLinks = document.getElementsByClassName('main-link');
let mainLinksLenght = mainLinks.length;
for(var i = 0; i < mainLinksLenght; i++){
    if(mainLinks[i].href==document.URL){
        mainLinks[i].classList.add('mainlink-active')
    }
}
