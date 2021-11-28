let bg = document.getElementById('parallax-bg');
let mid = document.getElementById('parallax-m');
let fr = document.getElementById('parallax-fr');

window.addEventListener('scroll', function() {
    let value = window.scrollY;
    if(value> -10)
    {
    	bg.style.top =  value * -0.04 + 'vh';
    	mid.style.top = value * -0.20 + 'vh';
    }
})
