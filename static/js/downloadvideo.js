$(function() {

  $('#buttonDownload').bind('click', function(event) {
    $.ajax({
      url: '/downloadVideo',
      data: $('#formDownload').serialize(),
      type: 'POST',
      success: function(resp) {
        var json = JSON.parse(resp);
        $('#respMessage').prepend(json.html);
      },
      error: function(err) {
        $('#respMessage').prepend('<span>Internal error!</span><br>');
      }
    });
  });

  $('#inputURI').bind('keypress', function(event) {
    if(event.which == 13) {
      event.preventDefault();
      $('#buttonDownload').click();
    }
  });

});
