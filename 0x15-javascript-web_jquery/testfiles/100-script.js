// Hold for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function () {
  const headerElement = document.querySelector('header');

  // Checking if header element is found the set color to red
  if (headerElement) {
    headerElement.style.color = '#FF0000';
  }
});
