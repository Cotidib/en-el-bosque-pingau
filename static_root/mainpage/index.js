function handleDirectBtnHover(e){
    let targetBtn = e.target.parentElement;
    console.log(targetBtn)
    let btnsContainer = targetBtn.parentElement;
    let workItem = btnsContainer.parentElement;
    let image = workItem.getElementsByClassName('work-img');
    image[0].classList.remove('image-filter-active');
   
}


function handleDirectBtnHoverOut(e){
    let targetBtn = e.target.parentElement;
    let btnsContainer = targetBtn.parentElement;
    let workItem = btnsContainer.parentElement;
    let image = workItem.getElementsByClassName('work-img');
    image[0].classList.add('image-filter-active');
}