$(function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    let helloData = data.hello;
    $("DIV#hello").text(helloData);
  });
});



