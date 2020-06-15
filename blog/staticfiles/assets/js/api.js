const apiData = {
    url: 'http://127.0.0.1:8000/contatos/'
}

const contact_form = document.getElementById("contact_form");

contact_form.addEventListener("submit", (e) => {
    e.preventDefault();
    
    const request = new XMLHttpRequest();
    request.open(contact_form.method, apiData.url);
    request.onload = function () {
        //console.log(request.readyState)
        //console.log(request.status)
    
        if (request.status === 201 && request.readyState === 4)
            alert("MENSAGEM ENVIADA!!!");
        else
            alert("ALGO DE ERRADO N ESTA CERTO, MENSAGEM NAO ENVIADA!!!");

        //console.log(request.responseText);
    }
    formData = new FormData(contact_form)
    request.send(formData);

    contact_form.reset();
});