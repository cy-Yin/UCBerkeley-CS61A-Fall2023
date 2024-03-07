var gui;
$.ajaxSetup({
        async: false,
        cache: false,
});

function GUI() {
    this.oldState;
    this.newState;
    this.stateInitialised = false;
    this.deadbees = [];
    this.deadinsects = [];
    this.locToAnt = [];
}

function updateControlPanel() {
    let tr = $('#antsTableRow');
    tr.find('td').each(function() {
        let name = $(this).attr('data-name');
        let cost = $(this).attr('data-cost');
        let disabled = $(this).attr('data-disabled');
        if (disabled == 1 && gui.get_food() >= cost) {
            $(this).attr("data-disabled", 0).removeClass("ant-inactive");
        }
        else if (disabled == 0 && gui.get_food() < cost) {
            $(this).attr("data-disabled", 1).addClass("ant-inactive");
        }
    });
}
function drawControlPanel(food, places, ants) {
    let tr = $('#antsTableRow');
    for (var id in ants) {
        let ant = ants[id];
        if (ant["cost"] > food)
            tr.append('<td data-disabled="1" data-cost="' + ant["cost"] + '" data-img="' + ant["img"] + '" data-name="' + ant["name"] + '" id="ant_' + ant["name"]  + '" class="ant-row ant-inactive"><img class="ant-img" src="' + ant["img"] + '"> ' + ant["name"] + '<hr class="ant-row-divider" /><span class="badge ant-cost">' + ant["cost"] + '</span></td>');
        else
            tr.append('<td data-disabled="0" data-cost="' + ant["cost"] + '" data-img="' + ant["img"] + '" data-name="' + ant["name"] + '" id="ant_' + ant["name"] + '" class="ant-row"><img class="ant-img" src="' + ant["img"] + '"> ' + ant["name"] + '<hr class="ant-row-divider" /><span class="badge ant-cost">' + ant["cost"] + '</span></td>');
    }
    updateFoodCount();
    drawInitialPlaces();
}

function drawInitialPlaces() {
    let pTable = $('.places-table');
    let rows = gui.get_rows();
    let places = gui.get_newPlaces();
    let i = 0;
    let tr = null;
    while (i < rows) {
        pTable.append('<tr id="pRow' + i + '"></tr>');
        tr = pTable.find('#pRow' + i);
        for (col in places[i]) {
            let random_sky = Math.floor(Math.random() * 3) + 1;
            let random_ground = Math.floor(Math.random() * 3) + 1;
            if (places[i][col]["water"] == 1) {
                random_ground = "water";
            }
            tr.append('<td data-row="' + i  + '" data-col="' + col  + '" data-name="' + places[i][col]["name"]  + '" class="places-td" id="pCol' + col + '"><div class="tunnel-div"><div class="tunnel-img-container"></div><div style="background-image: url(\'assets/tiles/sky/' + random_sky + '.png\')"class="tunnel-goc-div"></div><div style="background-image: url(\'assets/tiles/ground/' + random_ground + '.png\')" class="tunnel-goc-div"></div></div></td>');
        }
        i += 1;
    }

    let hiveContainer = $('.hive-container');
    hiveContainer.append('<div id="beehive" class="beehive"></div>')
    let hive = hiveContainer.find('.beehive');
    for (bee in places["Hive"]["insects"]) {
        hive.append(make_img_tag("assets/insects/bee.gif", {'data-id': bee, 'class': "bee-img"}));
    }
}

function updateFoodCount() {
    $('#foodCount').html(gui.get_food());
}

function startGame() {
    gui = new GUI();
    gui.startGame();
    gui.get_gameState(false);
    drawControlPanel(gui.get_food(), gui.get_newPlaces(), gui.get_antTypes());
    gui.strategyTime = gui.get_strategyTime();
    gui.interval = setInterval(gui.update.bind(gui), 500);
}

GUI.prototype.startGame = function() {
    $.ajax({
        type: 'POST',
        url: 'ajax/start/game',
        async: false,
    });
}
GUI.prototype.get_localGameState = function() {
    return this.newState;
}
GUI.prototype.get_gameState = function() {
    let t = this;
    $.ajax({
      type: 'POST',
      url: 'ajax/fetch/state',
      async: false,
      success: function(state){
        if(!gui.initialised) gui.initialised = true
        t.updateState(state);
        return state;
      }
    })
    .fail(function(xhr, tStatus, e) {
        if(!gui.initialised){
          setTimeout(gui.get_gameState(), 500)
        }else{
          swal({
              title: "Error",
              text: e,
              type: "error",
              showConfirmButton: false,
              });
        }
    });
};

GUI.prototype.get_winner = function() {
    return this.newState["winner"];
}
GUI.prototype.get_rows = function() {
    return this.newState["rows"];
}

GUI.prototype.updateState = function(s) {
    this.oldState = this.newState;
    this.newState = s;
}

GUI.prototype.get_antTypes = function() {
    return this.newState["ant_types"];
}

GUI.prototype.get_newPlaces = function() {
    return this.newState["places"];
}

GUI.prototype.get_oldPlaces = function () {
    return this.oldState["places"];
}

GUI.prototype.get_food = function() {
    return this.newState["food"];
}
GUI.prototype.selectAnt = function(name, img) {
    this.selected_ant = { name: name, img: img };
}
GUI.prototype.get_beeToId = function() {
    return this.newState["beeToId"];
}
GUI.prototype.get_beeLocations = function() {
    return this.newState["beeLocations"];
}
GUI.prototype.get_oldBeeLocations = function() {
    return this.oldState["beeLocations"];
}
GUI.prototype.deselectAnt = function() {
    currentSelected = this.get_selectedAnt();
    this.selected_ant = null;
    if (currentSelected) {
        $('#antsTableRow').find("[data-name = '" + currentSelected["name"] + "']").removeClass("ant-selected");
    }
}
GUI.prototype.get_selectedAnt = function() {
    return this.selected_ant;
}
GUI.prototype.get_time = function() {
    return this.newState["time"];
}
GUI.prototype.is_gameOver = function() {
    return this.newState["gameOver"];
}
GUI.prototype.updateTime = function() {
     $('#timeCount').html(this.get_time());
}
GUI.prototype.get_strategyTime = function() {
    return this.newState["strategyTime"];
}
GUI.prototype.get_deadbees = function() {
    return this.newState["deadbees"];
}
GUI.prototype.get_deadinsects = function() {
    return this.newState["deadinsects"];
}
GUI.prototype.clearBoard = function(){
  $(".places-table > tbody").empty();
  $(".hive-container").empty();
}
GUI.prototype.clearAntTypes = function(){
  $("#antsTableRow").empty();
}

GUI.prototype.restartGame = function(){
  this.clearBoard();
  this.clearAntTypes();
  startGame();
}

$('#antsTableRow').on('click', ".ant-row", function() {
    let currentSelected = gui.get_selectedAnt();
    if (currentSelected) {
        $('#antsTableRow').find("[data-name = '" + currentSelected["name"] + "']").removeClass("ant-selected");
        gui.deselectAnt()
    }
    if (!currentSelected || currentSelected["name"] != $(this).attr('data-name')) {
        $(this).addClass('ant-selected');
        gui.selectAnt($(this).attr('data-name'), $(this).attr('data-img'));
    }
});


$("#playBtn").on('click', function() {
    $(this).addClass('animated fadeOutLeft');
    $('#header-title').addClass('animated fadeOutUp');
    $('#hero-head').addClass('animated bounceOutDown').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
        $('#hero-head').hide();
        //Load the game wrapper and bg
        $('#gameWrapper').show().addClass('animated bounceInDown');
    });
    startGame();
});

$('#exitBtn').on('click', function() {
    clearInterval(gui.interval);
    $.post("ajax/exit");
    swal({
        title: "Terminated",
        text: "The Web GUI has been killed.",
        type: "warning",
        showConfirmButton: false,
        });
});

$('.places-table').on('click', '.places-td', function() {
    //Check to see if an insect is selected
    let t = this
    let selectedAnt = gui.get_selectedAnt();
    if (!selectedAnt) {
        swal({
            title: "Error",
            text: "You need to select an insect first.",
            type: "error",
        });
    }
    if (selectedAnt["food"] > gui.get_food()) {
        swal({
            title: "Error",
            text: "Not enough food remains to place " + selectedAnt["name"],
            type: "error",
        });
    }
    $.ajax({
        method: "POST",
        url: "ajax/deploy/ant",
        data: { pname: $(this).attr("data-name"), ant: selectedAnt["name"]},
    })
        .done(function(response) {
            if (response["error"]) {
                swal({
                    title: "Error",
                    text: response["error"],
                    type: "error",
                });
            }
            else {
                //$(t).find('.tunnel-img-container').html('<img data-id="' + response["id"]  +'" class="active-ant" src="' + selectedAnt["img"]  + '">');
                let r = $(t).attr("data-row");
                let c = $(t).attr("data-col");
                if (!gui.locToAnt[r]) gui.locToAnt[r] = [];
                if(!gui.locToAnt[r][c]){
                  gui.locToAnt[r][c] = [response["id"]];
                }else{
                  // container
                  gui.locToAnt[r][c].unshift(response["id"]);
                }
                gui.update();
            }
        });
});

GUI.prototype.moveBees = function() {
    let newLocation = this.get_beeLocations();
    let oldLocation = this.get_oldBeeLocations();
    let locNameToNumBees = {};
    for (let bee in newLocation) {
        let locName = newLocation[bee]
        let loc = $('.places-table').find('td[data-name="' + locName + '"]');
        let img = $('.bee-img[data-id="' + bee  + '"]');
        // To allow for bee overlap, we offset adjacent bees
        if (!locNameToNumBees.hasOwnProperty(locName)) {
            locNameToNumBees[locName] = 0
        }
        let numBees = locNameToNumBees[locName];
        let newPosition = {
            "left": 0 + 5 * numBees,
            "top": 25 + 5 * numBees,
            "position": "absolute",
        }
        locNameToNumBees[locName]++
        if (oldLocation[bee] != locName) { // If no change
            loc.find('.tunnel-img-container').append(img)
        }
        img.css(newPosition)
    }
    let db = this.get_deadbees();
    for (let b in db) {
        if ($.inArray(db[b], this.deadbees) == -1) {
            //We have some bee killing to do
            $('.bee-img[data-id="' + db[b] + '"]').hide("explode", {pieces: 16}, 1000);
            this.deadbees.push(db[b]);
        }
    }
}

GUI.prototype.updateAnts = function() {
    let oldPlaces = this.get_oldPlaces();
    let newPlaces = this.get_newPlaces();
    for (let r in newPlaces) {
        if (r == "Hive") {
            continue;
        }
        for (let c in newPlaces[r]) {
            let oldAnt = oldPlaces[r][c]["insects"]
            let newAnt = newPlaces[r][c]["insects"]
            if (newAnt.hasOwnProperty("type") && (!oldAnt.hasOwnProperty("id") || oldAnt.id != newAnt.id)) {
              let antImgTag =  make_img_tag(newAnt["img"],{"data-id":gui.locToAnt[r][c][0], "class":"active-ant", "container":newAnt["container"]})
              if(newAnt["container"] && newAnt["contains"]){
                antImgTag = make_img_tag(newPlaces[r][c]["insects"]["contains"]["img"], {"class":"contained-ant"}) + antImgTag;
              }
              $('.places-table').find('.places-td[data-row="' + r  + '"][data-col="' + c  + '"]').find('.tunnel-img-container').append(antImgTag);
            }
        }
    }
    let di = this.get_deadinsects();
    for (let a in di) {
        if ($.inArray(a, this.deadinsects) == -1) {
            //We have some ant killing to do lol -CS

            let img = $('.places-table').find('.active-ant[data-id="' + di[a] + '"]')
            img.hide("explode", {pieces: 16}, 1000);
            if(img[0]){
              let td = img[0].closest("td");
              let r = $(td).attr("data-row");
              let c = $(td).attr("data-col");
              gui.locToAnt[r][c].shift();
            }
            this.deadinsects.push(di[a]);
        }
    }
}
GUI.prototype.update = function() {
    if (this.is_gameOver()) {
        clearInterval(this.interval);
        if (gui.get_winner()) {
            swal({
                title: "Congratulations",
                text: "You successfully defeated the bees!",
                type: "success",
                confirmButtonColor: "#0b752b",
                confirmButtonText: "Restart?"
              },
              this.restartGame.bind(this)
            );
        } else {
            swal({
                title: "Tough Luck",
                text: "You lost and the bees live on.",
                type: "warning",
                confirmButtonColor: "#0b752b",
                confirmButtonText: "Restart?"
              },
              this.restartGame.bind(this)
            );
        }
        return;
    }
    this.get_gameState();
    updateControlPanel();
    this.updateTime();
    updateFoodCount();
    this.moveBees();
    this.updateAnts();
}

GUI.prototype.fireOff = function(){
  let beeLocations = this.get_beeLocations();
  let beeGrid = []
  let places = this.oldState.places;
  let height = keys(places).length - 1;
  let width = keys(places['0'].length);
  let ants = [];
  for(let i = 0; i < height; ++i){
    beeGrid.push(new Array(width));
  }
  for(let i = 0; i < beeLocations.length; ++i){
    location = beeLocations[i].split('_');
    beeGrid[ location[1] ][ location[2] ] = true;
  }
  for(let i = 0; i < height; ++i){
    for(let j = 0; j < width; ++j){
      ants = location[i+""][j+""]["insects"];
    }
  }
}

// particles.js
function shoot_from(a, b){
  console.log("fired from " + a + " to " + b);
}

//utils.js
function make_img_tag(src, attributes){
  tag = "<div ";
  for(var attr in attributes) tag += ' ' + attr + " = " + attributes[attr];
  tag += "><img src = '" + src + "'></div>"
  return tag
}