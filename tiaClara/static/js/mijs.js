$( document ).ready(function(){
    
    var menu = $('#pegado');
    var contenedor = $('#menu-contenedor');
    var menu_offset = menu.offset();
    // Cada vez que se haga scroll en la página
    // haremos un chequeo del estado del menú
    // y lo vamos a alternar entre 'fixed' y 'static'.
    $(window).on('scroll', function() {
    if($(window).scrollTop() > menu_offset.top) {
      menu.addClass('menu-fijo');
      $('.menu li a').animate({
                color: white,
            }, 5000, function() {
    // Animation complete.
        });
    } else {
      menu.removeClass('menu-fijo');
    }
  });





    //para el nosotros!
   /* $('#aparecer').hide();

    $(window).scroll(function (event) {
    var scroll = $(window).scrollLeft();
    if (scroll == 50) {
        $('#aparecer').fadeIn(5000);
    } else {
        $('#aparecer').hide();
    }
    });
*/
    /////////para el Footer!




/*$(window).scroll(function (event) {
        var position_nosotros = $('#inicio').position();
        var position_mermeladas = $('#mermeladas').position();
        var position_dulces = $('#dulces').position();
        var position_jaleas = $('#jaleas').position();
        var position_otros = $('#otros').position();
        var position_contacto = $('#contacto').position();

        if (posicion == position_nosotros) {
            $('.menu .selected').removeClass('selected');
            $(this).addClass('.activo');
        } 
        
        if(posicion == position_mermeladas){
            $('.menu .selected').removeClass('selected');
            $(this).addClass('activo');
        }

        if(posicion == position_dulces){
            $('.menu .selected').removeClass('selected');
            $(this).addClass('activo');
        }
        if(posicion == position_jaleas){
            $('.menu .selected').removeClass('selected');
            $(this).addClass('activo');
        }
        if(posicion == position_otros){
            $('.menu .selected').removeClass('selected');
            $(this).addClass('activo');
        }
        if(posicion == position_contacto){
            $('.menu .selected').removeClass('selected');
            $(this).addClass('activo');
        }
    });

*/


    $("#menu_principal li a").click(function () {
          $("#menu_principal li a").removeClass(".selected");    
          $(this).addClass(".selected");
    });
  






});