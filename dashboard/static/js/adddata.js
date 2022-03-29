    // Call hideShow when page is loaded
    $(document).ready(function(){
        hideShow()
    })

    // call hideShow when the user clicks on the id_events dropdownlist
    $('#id_events').click(function(){
        hideShow()
    });
    

function hideShow()
{
    if(document.getElementById('id_events').options[document.getElementById('id_events').selectedIndex].value == "Others")
    {
        $('#id_others').show();
    }
    else
    {
        
        $('#id_others').hide();
    }
    if(document.getElementById('id_events').options[document.getElementById('id_events').selectedIndex].value == "Coursera")
    {
        $('#id_coursera_types').show();
    }
    else
    {
        
        $('#id_coursera_types').hide();
    }

}