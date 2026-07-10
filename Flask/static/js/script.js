document.addEventListener("DOMContentLoaded", function () {

    console.log("Smart Lender Loaded Successfully");

    const form = document.querySelector("form");

    if(form){

        form.addEventListener("submit", function(){

            const btn = document.querySelector("button[type='submit']");

            if(btn){

                btn.innerHTML = "⏳ Predicting...";

                btn.disabled = true;

            }

        });

    }

});