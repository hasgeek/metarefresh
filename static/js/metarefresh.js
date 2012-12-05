

$(function() {

  // fixed nav-bar transition code
  // adapted from twitter bootstrap docs' sub-nav

  var $win = $(window)
    , $nav = $('.navbar')
    , navTop = $nav.length && $nav.offset().top // - 40
    , isFixed = 0;
  
  var processScroll = function () {
    var scrollTop = $win.scrollTop();
    if (scrollTop >= navTop && !isFixed) {
      isFixed = 1;
      $nav.addClass('navbar-fixed-top');
    } else if (scrollTop <= navTop && isFixed) {
      isFixed = 0;
      $nav.removeClass('navbar-fixed-top');
    };
  };
  
  processScroll();
  
  $win.on('scroll', processScroll);
  
  // smooth scroll nav links
  $('a', $nav).smoothScroll({
      offset: -80
    , speed: 900
  });

});
