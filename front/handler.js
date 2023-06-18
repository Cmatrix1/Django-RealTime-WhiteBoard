$(() => {
	const w = $('body').width()
	$('.preload').fadeOut(1000)
	if (w < 576) {
		$('#rightBox').hide()
		$('#rightBox').css({
			position: 'absolute',
			width: '100%',
			hight: '100%',
		})
	}
	$('#fabChat').click(function () {
		$('#rightBox').toggle(1000)
		$('.fab').toggleClass('position-absolute')
		$('#fabMenu').toggle()
		$('#fabChat i').toggleClass('fa-close fa-comment')
	})
})
