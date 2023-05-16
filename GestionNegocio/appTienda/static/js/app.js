$(function(){
  $("#fileFoto").on("change",mostrarImagen);
})

function abrirModalEliminar(idProducto) {
    Swal.fire({
      title: "Eliminar Producto",
      text: "¿Estas seguro de eliminar?",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#00b347",
      cancelButtonColor: "#d33",
      cancelButtonText: "NO",
      confirmButtonText: "SÍ",
    }).then((result) => {
      if (result.isConfirmed) {
        location.href="/eliminarProducto/"+idProducto+"/"
      }
    });
  }

  function mostrarImagen(evento) {
    const archivos = evento.target.files
    const archivo = archivos[0]
    const url = URL.createObjectURL(archivo)

    $("#imagenProducto").attr("src",url)

  }

    
    /*let files = evt.target.files;
    var fileName = files[0].name;
    var fileSize = files[0].size;
    let extension = fileName.split(".").pop();
    extension = extension.toLowerCase();
    if (extension !== "jpg"){
      Swal.fire("Cargar Imagen",'La imagen debe tener una extensión JPG','warning')
      $("#fileFoto").val(""); 
      $("#fileFoto").focus();
    } else if (fileSize > 50000){
      Swal.fire("Cargar Imagen",'La imagen NO puede superar los 50K','warning')
      $("#fileFoto").val("");
      $("#fileFoto").focus();
    }
    
  }*/
  