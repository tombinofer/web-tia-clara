$(document).ready(function(){

 $(".accordion ul").hide();

 $(".accordion h2").click(function(){
 $(this).next("ul").slideToggle("slow")
 .siblings("ul:visible").slideUp("slow");
 $(this).toggleClass("active");
 $(this).siblings("h2").removeClass("active");
 });

});