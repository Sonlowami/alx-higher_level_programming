const target = $('header');
$('#toggle_header').bind('click', () => {
  if (target.hasClass('red')) {
    target.removeClass('red');
    target.addClass('green');
  } else if (target.hasClass('green')) {
    target.removeClass('green');
    target.addClass('red');
  }
});
