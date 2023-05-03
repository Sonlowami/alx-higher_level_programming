$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  (data, status) => {
    $.each(data.results, (index, movie) => {
      $('#list_movies').append($('<li></li>').text(movie.title));
    });
  });
