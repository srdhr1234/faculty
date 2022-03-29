    // Call hideShow when page is loaded
    $(document).ready(function(){
        hideShow()
    })

    // call hideShow when the user clicks on the id_events dropdownlist
    $('#id_event_type').click(function(){
        hideShow()
    });
    

function hideShow()
{
    if(document.getElementById('id_event_type').options[document.getElementById('id_event_type').selectedIndex].value == "Others")
    {
        $('#id_others').show();
    }
    else
    {
        
        $('#id_others').hide();
    }

}