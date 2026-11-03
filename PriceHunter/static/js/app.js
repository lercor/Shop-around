const fileInput = document.getElementById("product_image");
const fileName = document.getElementById("file-name");
if (fileInput && fileName) {
  fileInput.addEventListener("change", () => {
    const file = fileInput.files && fileInput.files[0];
    fileName.textContent = file ? `已選擇：${file.name}` : "";
  });
}
