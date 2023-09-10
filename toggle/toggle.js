const toggle = document.getElementById('darkMode');
const body = document.querySelector('body');


toggle.addEventListener('click',function(){
    this.classList.toggle('bi-moon-fill');
    if(this.classList.toggle('bi-brightness-high-fill')){
        body.style.background='white';
        body.style.color='black'
        body.style.transition='0.6s'
    }
    else{
        body.style.background='black';
        body.style.color='white';
        body.style.transition="0.6s"
    }
})