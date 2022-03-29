(function ($) {
    //    "use strict";
    console.log("1");

    /*  Data Table
    -------------*/

 	// $('#bootstrap-data-table').DataTable();


    $('#bootstrap-data-table').DataTable({
        lengthMenu: [[100, 25, 50, -1], [100, 25, 50, "All"]],
    });
	console.log("2");


    $('#bootstrap-data-table-export').DataTable({
        dom: 'lBfrtip',
        lengthMenu: [[100, 25, 50, -1], [100, 25, 50, "All"]],
        buttons: [

        ]
    });
	console.log("3");

	$('#row-select').DataTable( {
			initComplete: function () {
				this.api().columns().every( function () {
					var column = this;
					var select = $('<select class="form-control"><option value=""></option></select>')
						.appendTo( $(column.footer()).empty() )
						.on( 'change', function () {
							var val = $.fn.dataTable.util.escapeRegex(
								$(this).val()
							);
	 
							column
								.search( val ? '^'+val+'$' : '', true, false )
								.draw();
						} );
	 
					column.data().unique().sort().each( function ( d, j ) {
						select.append( '<option value="'+d+'">'+d+'</option>' )
					} );
				} );
			}
		} );
	console.log("4");





})(jQuery);