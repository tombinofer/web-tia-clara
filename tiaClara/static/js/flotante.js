$( document ).ready(function(){

    $('.nav .flotante').hide();

    $(window).scroll(function (event) {
    var scroll = $(window).scrollTop();
    if (scroll > 100) {
        $('.nav .flotante').show();
    } else {
        $('.nav .flotante').hide();
    }
    });
});