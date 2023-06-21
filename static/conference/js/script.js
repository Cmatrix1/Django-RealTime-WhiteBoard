const App = () => {
    return React.createElement(
        React.Fragment,
        null,
        React.createElement(
            "div",
            {
                style: { height: "100%" },
            },
            React.createElement(ExcalidrawLib.Excalidraw)
        )
    );
};

const excalidrawWrapper = document.getElementById("app");
const root = ReactDOM.createRoot(excalidrawWrapper);
root.render(React.createElement(App));



// Buttons Events
$(".leave-btn").click(() => window.location = "/" );


// Method For Send The Board To Backend
function saveCanvasImage(canvas) {
    canvas.toBlob(function (blob) {
      var formData = new FormData();
      formData.append('image', blob, 'canvas_image.png');
  
      $.ajax({
        url: '/api//image/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function (data) {
          console.log('Image saved:', data.file_path);
        },
        error: function (jqXHR, textStatus, errorThrown) {
          console.error(errorThrown);
        }
      });
    });
  }