const $hElem = $('header');
const $divRH = $('div#red_header');

$divRH.on('click', function () {
  $hElem.css('color', '#FF0000');
});
