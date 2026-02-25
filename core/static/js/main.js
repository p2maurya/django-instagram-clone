console.log("Instagram Clone Loaded 🚀");
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".like-btn").forEach(button => {
        button.addEventListener("click", function () {
            this.classList.add("animate-like")
            setTimeout(() => {
                this.classList.remove("animate-like")
            }, 300)
        })
    })
})