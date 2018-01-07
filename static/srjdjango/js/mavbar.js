$(document).on("ready",function() {
  // 0 = hide, 1 = visible
  var menuState = 0;
  //if($(".mini-menu-options").is(":hidden")) {
    /* Add a Click event listener to btn-select */
    $(".btn-select").on("click",function() {
      if(menuState === 0) {
        $(".mini-menu-options").slideDown("slow");
        menuState = 1;
      } else {
        $(".mini-menu-options").slideUp("slow");
        menuState = 0;
      }
    });
  //}
  $(".mini-menu-options li").on("click", function() {
    var numHijos = $(this).children().length;
    if(numHijos < 2) {
      // hide the menu
      $(".mini-menu-options").hide("fast");

      var texto = $(this).text();

      $(".menu-select .menu-actual").text(texto);
    }
    menuState = 0;
  });
});

var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-36251023-1']);
  _gaq.push(['_setDomainName', 'jqueryscript.net']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
