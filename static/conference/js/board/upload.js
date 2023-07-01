// Method For Send The Board To Backend

function saveCanvasImage() {
    canvas = document.querySelector('canvas')
    canvas.toBlob(function (blob) {
      var formData = new FormData();
      formData.append('image', blob, 'canvas_image.png');
      console.log(formData);
      $.ajax({
        url: `/board/api/${roomSlug}/save-image/`,
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        cache: false,
        success: function (data) {
          showNotification('Image Saved: '+ data.file_path)
        },
        error: function (jqXHR, textStatus, errorThrown) {
          console.error(errorThrown);
          showNotification('Error In Saving The Board !')
        }
      });
    });
  }

document.querySelectorAll("#upload-board").forEach(element => {
    console.log(element);
    element.onclick = saveCanvasImage
});