$(document).ready(function(){

 $(".accordion ul").hide();

 $(".tipos").click(function(){
 $(this).next("ul").slideToggle("slow")
 .siblings("ul:visible").slideUp("slow");
 $(this).toggleClass("active");
 $(this).siblings(".tipos").removeClass("active");
  
   });
});