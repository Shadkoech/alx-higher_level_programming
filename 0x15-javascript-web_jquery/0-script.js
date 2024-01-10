// Hold for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // Selecting the <header> element using document.querySelector
  const headerElement = document.querySelector('header');

  // check if the header element has been found
  if (headerElement) {
    headerElement.style.color = '#FF0000';
  }
});
