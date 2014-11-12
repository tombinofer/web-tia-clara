$("#formContact").validate({
  invalidHandler: function(event, validator) {
    // 'this' refers to the form
    var errors = validator.numberOfInvalids();
    if (errors) {
      var message = errors == 1
        ? 'Se encontró 1 campo con error. Está resaltado!'
        : 'Se encontró ' + errors + ' campos con errores. Están resaltados';
      $("div.error span").html(message);
      $("div.error").show();
    } else {
      $("div.error").hide();
    }
  }
});



