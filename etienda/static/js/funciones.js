function asignarUsuario(idUsuario){
    document.getElementById('idUsuario').value = idUsuario;
}

$('#id_estado').change(function(e){
    let token = $('[name="csrfmiddlewaretoken"]').val();
    let url = $(this).data('url');
    $.ajax({
        type: 'POST',
        url: url,
        data: {'id_estado':$(this).val(), 'csrfmiddlewaretoken':token },
        success: function(data){
            let html= '';
            $.each(data, function(llave,valor){
                html += `<option value="${valor.id}">${valor.nombre} </option>`
            });
            $('#id_municipio').html(html);
        }
    });
});