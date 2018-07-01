// Temporary solution, hopefully
var globals = {};
globals.filters = [];


/* Custom filtering function which will search data in column four between two values */
$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        if (globals.filters[0]){
            var columnIndex = globals.filters[0].columnIndex;
            var imgAlt = data[columnIndex];
            
        }
        var min=2, max=4, age=3;
 
        if ( ( isNaN( min ) && isNaN( max ) ) ||
             ( isNaN( min ) && age <= max ) ||
             ( min <= age   && isNaN( max ) ) ||
             ( min <= age   && age <= max ) )
        {
            return true;
        }
        return false;
    }
);
 

$(document).ready(function() {
    var table = $('#example').DataTable({
        "columns": [
            { "orderable": false },
            null,
            { "orderable": false },
            null,
            null,
            null
          ],
        "order": [[ 1, 'asc' ]]
    });

    // Event listener to the two range filtering inputs to redraw on input
    $('#min, #max').keyup( function() {
        table.draw();
    });

    globals.filters.push({
        'filterValue': '',
        'columnIndex': 5
    });

    $('.ui.dropdown')
      .dropdown({
        "selectOnKeydown": false,
        onAdd: function(addedValue, addedText, $addedChoice) {
            console.log(addedValue);
            console.log(addedText);
            console.log($addedChoice);
            globals.filters[0].filterValue = addedText;
            table.draw();
        },
        onRemove: function(removedValue, removedText, $removedChoice) {

            console.log('RemovedRemovedRemovedRemovedRemovedRemovedRemovedRemovedRemoved');
        }
      })
    ;

});