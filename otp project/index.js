

const btn = document.getElementById(`submit`);

btn.onclick = function() {
    let input = document.getElementById(`text`);

    let input_text = Number(input.value);

    console.log(input_text);

    console.log(typeof input_text)
};