const receive_otp = document.getElementById('receive_otp');

const verify_btn = document.getElementById('submit');

let min = 1000;
let max = 9999;

const rand_otp = Math.floor((Math.random() * (max-min)) + min);

window.onload = function() {

    if(window.location.pathname.includes('otp_page_2.html')){
        window.alert(`Your OTP is ${rand_otp}`);
    }

};



verify_btn.onclick = function() {

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
        alert("Sorry, OTP don't match!!");
    }
};

