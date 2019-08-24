// Select color input
var color = document.getElementById('colorPicker');
// Select size input
var sizePicker = document.getElementById('sizePicker');
var table = document.getElementById('pixelCanvas');
//declare the other variables
var height = document.getElementById('inputHeight').value;
var width = document.getElementById('inputWidth').value;
makeGrid(height, width);

// When size is submitted by the user, call makeGrid()
sizePicker.addEventListener('click', function(event) {
    event.preventDefault();
    var height = document.getElementById('inputHeight').value;
    var width = document.getElementById('inputWidth').value;
    table.firstElementChild.remove();
    makeGrid(height, width);
});
//create function to make the grid and color the cells
function makeGrid(height, width) {

    for (var r = 0; r < height; r++) {
        var row = table.insertRow(r);
        for (var c = 0; c < width; c++) {
            var cell = row.insertCell(c);
            cell.addEventListener('click', function(event) {
                event.target.style.backgroundColor = color.value;
            });
        }
    }
}
