
// fixed nav-bar transition code
// adapted from twitter bootstrap docs' sub-nav

$(function() {
	var   $win = $(window)
		, $nav = $('.navbar')
		, navTop = $nav.length && $nav.offset().top// - 40
		, isFixed = 0
	
	function processScroll() {
		var scrollTop = $win.scrollTop()
		if (scrollTop >= navTop && !isFixed) {
			isFixed = 1
			$nav.addClass('navbar-fixed-top')
		} else if (scrollTop <= navTop && isFixed) {
			isFixed = 0
			$nav.removeClass('navbar-fixed-top')
		}
	}
	
	processScroll()
	
	$win.on('scroll', processScroll)
	
})

