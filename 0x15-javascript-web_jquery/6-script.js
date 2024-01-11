const $hElem = $('header');
const $updateHeaderElem = $('div#update_header');

$updateHeaderElem.on('click', () => {
  $hElem.text('New Header!!!');
});