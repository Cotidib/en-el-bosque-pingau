//JS LIBRARIES 
// https://masonry.desandro.com/
// https://infinite-scroll.com/
// https://imagesloaded.desandro.com/


var elem = document.querySelector('#m-gallery');

imagesLoaded( elem, () => {
    var msnry = new Masonry( elem, {
    // options
        itemSelector: '.m-item',
        columnWidth: 400,
        gutter: 5,
        isFitWidth: true,
      });

} )
