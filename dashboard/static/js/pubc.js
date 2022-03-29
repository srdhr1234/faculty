    // Call hideShow when page is loaded
    $(document).ready(function(){
        hideShow()
    })

    // call hideShow when the user clicks on the id_events dropdownlist
    $('#id_scopus').click(function(){
        hideShow()
    });
    

function hideShow()
{
    if(document.getElementById('id_scopus').options[document.getElementById('id_scopus').selectedIndex].value == "Yes")
    {
        $('#id_scopus_value').show();
    }
    else
    {
        
        $('#id_scopus_value').hide();
    }

}