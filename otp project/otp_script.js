const receive_otp = document.getElementById('receive_otp');

const verify_btn = document.getElementById('submit');

let min = 1000;
let max = 9999;

const rand_otp = Math.floor((Math.random() * (max-min)) + min);

window.onload = function() {

    if(window.location.pathname.includes('otp_page_2.html')){
        window.alert(`Your OTP is ${rand_otp}`);
    }

    else if (performance.navigation.type === performance.navigation.TYPE_RELOAD){
        window.location.href = 'otp_page1.html';
    };

};



verify_btn.addEventListener('click', async() => {
    let inputs = document.querySelectorAll(`.boxes .box`);
    let combined_string = '';

    inputs.forEach(input => {

        combined_string += input.value;
    });

    let otp_string = rand_otp.toString();

    if(otp_string === combined_string){
        window.location.href = 'otp_page3.html';
    }

    else{
        alert("Sorry, OTP not verified 😡!!");
    }

    
    const response = fetch('/submit', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({otp_string})
    })
    

    .then((response) => {
        if(response.ok){
            alert('Data sent successfully');
        }
        else{
            alert('Error sending data');
        }
    })
    
    .catch((error) => alert(`Request failed ${error.message}`))


});
