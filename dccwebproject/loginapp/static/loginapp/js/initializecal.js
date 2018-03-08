$(document).ready(function() {
  'use strict'
  var myevents = [];
  var curdate;

  //fullcalendar
  $('#calendar').fullCalendar({

    editable: true,
    startEditable: true,
    eventLimit: true,
    allDayDefault: true,
    selectable: true,
    selectHelper: true,
    header: {
      left: 'prev,next today myCustomButton',
      center: 'title',
      right: 'month,agendaWeek,agendaDay'
    },

    events: myevents,
    color: 'yellow',
    textColor: 'black',

    //calendar date-selection function
    select: function(start, end, jsEvent, view) {
      var newdate = $('#calendar').fullCalendar('getDate');
      console.log(newdate);
      curdate = moment(start).format();
      $('#startdt').val(curdate);
      console.log(curdate);
      moment(end).format() + 1;
    },

    //calendar day-click function
    dayClick: function() {
      $('.modal').modal();
      $('#modal1').modal('open');
      $('#calendar').fullCalendar('renderEvent', event);
    },
  });
  //fullcalendar end

  //datepicker
  $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: true // Close upon selecting a date,
  });

  //modal-onclick function
  $('.modal-action').click(function() {
    var eventarr = [];
    var title1 = $('.validate').val();
    var start1 = $('#startdt').val();
    var end1 = $('#enddt').val();
    var desc = $('#event_desc').val();
    var eventobj = {
      title: title1,
      start: curdate,
      end: end1,
      description: desc
    };
    eventarr.push(eventobj);
    myevents.push(eventobj);
    //add event to calendar
    $('#calendar').fullCalendar('addEventSource', eventarr);
    $('#calendar').fullCalendar('rerenderEvents');
    console.log(myevents);
  })
});
