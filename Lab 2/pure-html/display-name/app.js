let countHTML = document.getElementById("name");
let dispName = document.getElementById("disp-name");
let clearBtn = document.getElementById("clear-btn");

dispName.addEventListener("click", () => {
    countHTML.innerHTML = "Abhinav Lugun";
})

clearBtn.addEventListener("click", () => {
    countHTML.innerHTML = "-";
})