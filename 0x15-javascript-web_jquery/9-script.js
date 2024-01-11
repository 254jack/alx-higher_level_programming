$(document).ready(function () {
  const uri = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const $hiElem = $('div#hello');

  function getSalut () {
    return $.get({
      url: uri,
      dataType: 'json'
    });
  }

  getSalut().then((res) => {
    $hiElem.text(res.hello);
  });
});
