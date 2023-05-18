// Get the current path

var path = window.location.pathname;

// If the path is not the home page, create the Home button
if (path !== '/') {
  // Create the button element
  var button = document.createElement('div');
  button.className = 'button';
  button.type = 'button';

  // Create the link element and set its href attribute
  var link = document.createElement('a');

  link.href = document.getElementById('home-url').getAttribute('data-url');
  link.innerHTML = 'Главная';

  // Append the link element to the button element
  button.appendChild(link);

  // Append the button element to the home-button div in the HTML
  var homeButton = document.getElementById('home-button');
  homeButton.appendChild(button);
}