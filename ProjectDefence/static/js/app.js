(function ($) {
  "use strict";

  var fn = {

    // Launch Functions
    Launch: function () {
      fn.Header();
      fn.ImageView();
      fn.Apps();
    },


    // header
    Header: function (){
      $(document.body).headroom({
        tolerance : 10
      });
    },




    // image view
    ImageView: function() {
      $('.lightbox').magnificPopup({
        type: 'image',
        closeOnContentClick: true,
        closeBtnInside: false,
        fixedContentPos: true,
        mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
        image: {
          verticalFit: true
        }
      });

      $('.gallery').each(function() { // the containers for all your galleries
          $(this).magnificPopup({
              delegate: 'figure > a', // the selector for gallery item
              type: 'image',
              mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
              gallery: {
                enabled:true
              }
          });
      });
    },





    // apps
    Apps: function () {

      // lavalamp
      $('.lavalamp').lavalamp({
        setOnClick: true,
        enableHover: false,
        margins: false,
        autoUpdate: true,
        duration: 200
      });


      // steps
      $('.next-step').click(function(){
        $('.nav-steps > .active').next('.nav-link').trigger('click');
      });

      $('.prev-step').click(function(){
        $('.nav-steps > .active').prev('.nav-link').trigger('click');
      });



      // smooth scroll
      $(function () {
        var scroll = new SmoothScroll('[data-scroll]');
      });



      // zoom
      $('.zoom').zoom();
      // $('.zoom-click').zoom({ on:'click' });


      // sub menu
      $('.dropdown-menu a.dropdown-toggle').on('click', function(e) {
        if (!$(this).next().hasClass('show')) {
          $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
        }
        var $subMenu = $(this).next(".dropdown-menu");
        $subMenu.toggleClass('show');


        $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function(e) {
          $('.dropdown-submenu .show').removeClass("show");
        });


        return false;
      });

    }
  };

  $(document).ready(function () {
    fn.Launch();
  });

})(jQuery);