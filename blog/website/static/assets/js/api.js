const apiData = {
    url: 'http://ulopes.xyz/contatos/'
    //url: 'http://127.0.0.1:8000/contatos/'
}

const contact_form = document.getElementById("contact_form");

contact_form.addEventListener("submit", (evt) => {

    var response = grecaptcha.getResponse();
    if(response.length == 0) { 
        alert("Por favor, verifique sua humanidade!"); 
        evt.preventDefault();
        return false;
    }
    
    const request = new XMLHttpRequest();
    request.open(contact_form.method, apiData.url);

    request.onload = function () {
        //console.log(request.readyState)
        //console.log(request.status)
    
        if (request.status === 201 && request.readyState === 4) {
            alert("MENSAGEM ENVIADA!!!");
            contact_form.reset();
        } else {
            alert("Algo de errado não está certo, MENSAGEM NÃO ENVIADA!!!");
            //console.log(request.responseText);
        }
    }

    formData = new FormData(contact_form)
    request.send(formData);
    
    
});