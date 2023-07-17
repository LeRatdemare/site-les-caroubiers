const thisScript = document.getElementById("plannings-construct")
console.log(thisScript.dataset.planningsUrl)
for (let i = 0; i < 10; i++) {
    const liElement = document.createElement("li");
    const liText = document.createTextNode(i);
    liElement.appendChild(liText)
    ulTags = document.getElementsByTagName("ul")
    for (tag of ulTags) {
        tag.appendChild(liElement);
    }
    console.log(i)
}

$.ajax({
    url: thisScript.dataset.planningsUrl,  // URL de votre vue Django qui renvoie les données
    method: 'GET',
    dataType: 'json',
    success: function (response) {
        var plannings = response;
        // Utilisez la variable dans votre script JavaScript
        console.log(plannings);
    },
    error: function (xhr, status, error) {
        console.error(error);
    }
});
