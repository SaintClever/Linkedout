let downloadBtn = document.getElementById("downloadButton")
let imageToDownload = document.getElementById("imageToDownload");

downloadBtn.addEventListener("click", function() {
  downloadImage();
});

let downloadImage = () => {
  let imgUrl = imageToDownload.src;

  // Create a temporary anchor element
  let a = document.createElement("a");
  a.href = imgUrl;
  a.download = "Linkedout image.png"; // Name of the downloaded file

  // Append anchor to body, trigger the click event, and remove the anchor
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
};