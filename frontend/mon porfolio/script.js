// active le menu bergur
document.addEventListener("DOMContentLoaded", () => {
  const menuIcon = document.getElementById("menu-icon");
  const navlist = document.getElementById("navlist");
  const overlay = document.getElementById("overlay");

  if (menuIcon && navlist && overlay) {
    menuIcon.addEventListener("click", () => {
      menuIcon.classList.toggle("active");
      navlist.classList.toggle("active");
      document.body.classList.toggle("open");
    });

    overlay.addEventListener("click", () => {
      menuIcon.classList.remove("active");
      navlist.classList.remove("active");
      document.body.classList.remove("open");
    });
  }
});  

// alterner entre les boutons à propos





const buttons = document.querySelectorAll('.about-btn button');
const contents = document.querySelectorAll('.content');


buttons.forEach((button, index) => {
  button.addEventListener ("click", () => {
    contents.forEach(content => content.style.display = 'none');
    contents[index].style.display = 'block';
    buttons.forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');
});
});


// portfolio fillter

var mixer = mixitup('.portfolio-gallery',{
  selectors:{
    target:'.portfolio-box'
  },
  animation:{
    duration:500
  }
});


// initialize swiperjs


var swiper = new Swiper('.mySwiper', {
  slidesPerView: 1,
  spaceBetween: 30,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  autoplay: {
    delay: 3000,               // ⏱ 3 secondes entre chaque slide
    disableOnInteraction: false,
  },
  breakpoints: {
    576: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    1200: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
  }
});



// skill progress bar


const first_skill = document.querySelector(".skill:first-child");
const sk_counters = document.querySelectorAll(".counter span"); // corrige "couter" -> "counter"
const progress_bars = document.querySelectorAll(".skills svg circle");

let skillsPlayed = false;

window.addEventListener("scroll", () => {
  if (!skillsPlayed) skillsCounter();
});

function hasReached(el) {
  let topPosition = el.getBoundingClientRect().top;
  return window.innerHeight >= topPosition + el.offsetHeight;
}

function updateCount(num, maxNum) {
  let currentNum = +num.innerText;
  if (currentNum < maxNum) {
    num.innerText = currentNum + 1;
    setTimeout(() => {
      updateCount(num, maxNum);
    }, 12);
  }
}

function skillsCounter() {
  if (!hasReached(first_skill)) return;

  skillsPlayed = true;

  sk_counters.forEach((counter, i) => {
    let target = +counter.dataset.target;
    // Calcule la valeur du stroke-dashoffset en fonction du pourcentage
    let strokeValue = 456 - 456 * (target / 100);
    
    // Définit la variable CSS personnalisée --target pour l'animation
    progress_bars[i].style.setProperty("--target", strokeValue);
    
    // Lance l'animation du texte compteur avec un léger délai
    setTimeout(() => {
      updateCount(counter, target);
    }, 400);
  });

  // Lance l'animation CSS sur tous les cercles
  progress_bars.forEach(p => {
    p.style.animation = "progress 2s ease-in-out forwards";
  });
}



// side progress bar

let calcScrollValue = () => {
  const scrollProgress = document.getElementById('progress');
  const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
  const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const scrollValue = (scrollTop / scrollHeight) * 100;

  if(scrollTop > 100){
    scrollProgress.style.display = "grid";
  } else {
    scrollProgress.style.display = "none";
  }

  // applique la progression conique
  scrollProgress.style.background = `conic-gradient(#e6006d ${scrollValue}%, #fff ${scrollValue}%)`;
};

// Ajoute le listener une seule fois
document.getElementById('progress').addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});

window.onscroll = calcScrollValue;
window.onload = calcScrollValue;



//  active menu

let section = document.querySelectorAll('section');
let menuLi = document.querySelectorAll("header  ul li a");
function activeMenu(){
  let len = section.length;
  while(--len && window.scrollY + 97 < section [len].offsetTop){}
  menuLi.forEach(sec => sec.classlist.remove("active"));
  menuLi[len].classList.add("active");
}

activeMenu();
window.addEventListener("scroll", activeMenu);


ScrollReveal({
  distance: "90px",
  duration: 2000,
  delay: 200,
  // reset: true,
});

ScrollReveal().reveal('.hero-info,.main-text,.proposal,.heading',{
  origin: "top"
});
ScrollReveal().reveal('.about-img,.fillter-buttons,.contact-info',{
  origin: "left"
});
ScrollReveal().reveal('.about-content,.skills',{
  origin: "right"
});

ScrollReveal().reveal('allServices,.portfolio-gallery,.blog-box,footer,.img-hero',{
  origin: "bottom"
});