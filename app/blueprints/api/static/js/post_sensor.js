const form = document.querySelector('#sensor-form');

async function postSensor() {
	form_data = new FormData(form);
	data = Object.fromEntries(form_data);

	try {
		const response = await fetch('/sensors/post-sensor', {
			method: 'POST',
			headers: {
				"Content-Type": "application/json; charset=utf-8"
		},
			body: JSON.stringify(data),
		});
		console.log(await response.json());
	} catch (e) {
		console.error(e);
	}

	window.location.replace('/sensors');
}

form.addEventListener('submit', (event) => {
	event.preventDefault();
	postSensor();
});
