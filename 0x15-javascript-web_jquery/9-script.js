$(() => {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    dataType: 'jsonp',
    type: 'GET',
    success: (data) => { console.log(data); }
  });
});
