const $hElem = $('header');
const $divRH = $('DIV#toggle_header');

$divRH.on('click', () => {
  const currentClass = $hElem.attr('class');

  if (currentClass === 'green') {
    $hElem.toggleClass(`${currentClass} red`);
  }

  if (currentClass === 'red') {
    $hElem.toggleClass(`${currentClass} green`);
  }
});
