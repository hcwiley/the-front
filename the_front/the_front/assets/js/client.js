$(window).ready(function(){
  $("body").scrollspy({target:"#sidebar", offset: 40});
  $("body").scrollspy('refresh');
  //$('[data-spy="scroll"]').each(function () {
    //$(this).scrollspy('refresh');
  //});
});
