/**
 * This line is using jQuery to wait for the document
 * to be loaded before executing the code inside the function.
 * The () => {} syntax defines an anonymous function that will
 * execute when the document is ready.
 */
$(() => {
	/**
	 * It gets the width of the body element and stores it in a variable 'w'.
	 */
	const w = $('body').width()
	/**
	 * This line selects all elements with the class preload
	 * to slowly fade them out over a duration of 1000ms (1 second).
	 */
	$('.preload').fadeOut(1000)
	/**
	 * This line starts an if statement that checks
	 * if the width of the body element (w) is less than 576 pixels:
	 * 1- hides the rightBox element.
	 * 2- ets the CSS properties of the element with the ID rightBox
	 * to make it fill the entire screen and position it absolutely.
	 *
	 */
	if (w < 576) {
		$('#rightBox').hide()
		$('#rightBox').css({
			position: 'absolute',
			width: '100%',
			hight: '100%',
		})
	}

	/**
	 * When the width of the window is less than 576 pixels,
	 * the code hides the "#rightBox" element and sets its position to absolute with
	 * a width and height of 100%. This is likely intended to make the element take up
	 * the full width of the screen on smaller devices.
	 *
	 * When the window width is greater than or equal to 576 pixels,
	 * the code shows the "#rightBox" element and sets its position to static with
	 * a width of 25% minus 20 pixels and a height of 100%. This is likely intended to make
	 * the element take up a fixed portion of the screen on larger devices.
	 */

	$(window).on('resize', function () {
		let win = $(this)
		if (win.width() < 576) {
			$('#rightBox').hide()
			$('#rightBox').css({
				position: 'absolute',
				width: '100%',
				hight: '100%',
			})
		} else {
			$('#rightBox').show()
			$('#rightBox').css({
				position: 'static',
				width: 'calc(25% - 20px)',
				hight: '100%',
			})
		}
	})

	// FIXME: Below buttons need fix to some resolution

	/**
	 *This line starts an event listener that listens for a click on the element with the ID fabChat
	 * 1- toggles the element with the ID rightBox, causing it to either show or hide over a duration of 1000ms.
	 * 2- toggles the class position-absolute on all elements with the class fab.
	 * 3- toggles the display of the element with the ID fabMenu.
	 * 4- Finally, toggles the classes fa-close and fa-comment on the icon inside the element with the ID fabChat.
	 */
	$('#fabChat').click(function () {
		$('#rightBox').toggle(1000)
		$('.fab').toggleClass('position-absolute')
		$('#fabMenu').toggle()
		$('#fabChat i').toggleClass('fa-close fa-comment')
	})
	/**
	 *This line starts an event listener that listens for a click on the element with the fabMenu
	 * 1- toggles the element with the ID smallMenu, causing it to either show or hide over a duration of 1000ms.
	 * 2- toggles the class position-absolute on all elements with the class fab.
	 * 3- toggles the display of the element with the ID fabChat.
	 * 4- Finally, toggles the classes fa-close and fa-comment on the icon inside the element with the ID fabMenu.
	 */
	$('#fabMenu').click(function () {
		$('#smallMenu').toggle(1000)
		$('.fab').toggleClass('position-absolute')
		$('#fabChat').toggle()
		$('#fabMenu i').toggleClass('fa-close fa-comment')
	})
})
