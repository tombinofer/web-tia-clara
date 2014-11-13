$( document ).ready(function(){

    $('.nav .flotante').hide();

    $(window).scroll(function (event) {
    var scroll = $(window).scrollTop();
    if (scroll > 100) {
        $('.nav .flotante').fadeIn();
        $('.nav .flotante li a').css("color","black");
        $('.nav .flotante li a:hover').css("color","#bab03e");

    } else {
        $('.nav .flotante').hide();
    }
    });
});