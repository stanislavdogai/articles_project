async function makeRequest(url, method='GET') {
    let response = await fetch(url, {method});

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

let like_article = async function (event){
    let url = event.target.dataset.articleUrl
    let data = await makeRequest(url)
    let p_id = event.target.dataset.id
    let button = event.target
    if (button.innerText == 'like'){
        button.innerText = 'unlike'
    }
    else {
        button.innerText = 'like'
    }
    let p = document.getElementById(`${p_id}`)
    p.innerText = `Лайки: ${data.article}`
}

let comment_like = async function (event){
    let url = event.target.dataset.articleUrl
    let data = await makeRequest(url)
    let p_id = event.target.dataset.id
    let button = event.target
    if (button.innerText == 'like'){
        button.innerText = 'unlike'
    }
    else {
        button.innerText = 'like'
    }
    let p = document.getElementById(`${p_id}`)
    p.innerText = `Лайки: ${data.comment}`
}
