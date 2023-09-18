$(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    let nameData = data.name;
    $("DIV#character").append(nameData);
  });
});