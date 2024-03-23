window.addEventListener("load",function(){
    this.setTimeout(
        function open(event){
           document.querySelector(".popup").style.display="block";
        },
        1000
    )
})
document .querySelector("#close").addEventListener("Click",function(){
           document.querySelector(".popup").style.display="none";
});