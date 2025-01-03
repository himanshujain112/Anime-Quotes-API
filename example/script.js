async function fetchAPI() {
	let response = await fetch(
		"https://anime-quotes-api-seven.vercel.app/random"
	);
	let text = await response.json();
	document.getElementById("animeTitle").innerHTML = text["anime"];
	document.getElementById("animeCharacter").innerHTML =
		"~ " + text["character"];
	document.getElementById("animeQuote").innerHTML = text["quote"];
}

fetchAPI();
