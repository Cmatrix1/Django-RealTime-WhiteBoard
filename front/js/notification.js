const notification = document.querySelector('#notification')
const text = document.querySelector('#notification-text')
const icon = document.querySelector('#notification-icon')

const showNotification = (t) => {
	text.textContent = t
	notification.classList.add('show')
	setTimeout(() => {
		notification.classList.remove('show')
	}, 5000)
}
