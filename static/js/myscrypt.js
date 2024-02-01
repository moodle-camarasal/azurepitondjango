const h1 = document.querySelector('h1');
let color = 'blue';

h1.addEventListener('click', () => {
  if (color === 'blue') {
    h1.style.color = 'red';
    color = 'red';
  } else {
    h1.style.color = 'blue';
    color = 'blue';
  }
});