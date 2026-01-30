console.log("JavaScript is connected 🚀");

document.addEventListener("DOMContentLoaded", () => {
    const btn = document.querySelector("button");

    btn.addEventListener("click", () => {
        btn.innerText = "Calculating...";
        setTimeout(() => {
            btn.innerText = "Calculate";
        }, 1000);
    });
});
