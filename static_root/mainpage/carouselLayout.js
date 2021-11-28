//https://nickpiscitelli.github.io/Glider.js/
//Initialize Glider Js

new Glider(document.querySelector('.glider'), {
    slidesToShow: 'auto',
    slidesToScroll: 'auto',
    itemWidth: 300,
    exactWidth: false,
    scrollLock: false,
    draggable: true,
    resizeLock: true,
    dragVelocity: 1,
    dots: '.dots',
    arrows: {
      prev: '.glider-prev',
      next: '.glider-next'
    },
  });