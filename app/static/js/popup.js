/*
    NAME:          popup.js
    AUTHOR:        Alan Davies (Lecturer Health Data Science)
    EMAIL:         alan.davies-2@manchester.ac.uk
    DATE:          18/12/2019
    INSTITUTION:   University of Manchester (FBMH)
    DESCRIPTION:   JavaScript file for managing display of popup dialoges
*/

function Popup()
{
    var popup = new Object();
    popup.mask = document.getElementById("page-mask");
    popup.entryFormPopup = document.getElementById("creat-calc");
    popup.aboutPopup = document.getElementById("about-box");

    // display the popup mask
    popup.showMask = function()
    {
        this.mask.style.display = "block";
        $('#page-mask').height($(document).height());
    }

    //hide the popup mask
    popup.hideMask = function()
    {
        this.mask.style.display = "none";
    }

    //show the creatinine clearance calculator form dialog
    popup.showCeatCalcFormPopup = function()
    {
        this.showMask();
        this.entryFormPopup.style.display = "block";
        this.positionDialogue(this.entryFormPopup);
        //this.entryFormPopup.style.left = (($(document).width() / 2) - (this.entryFormPopup.offsetWidth / 2)) + "px";
    }

    // hide the creatinine clearance calculator form dialog
    popup.hideCeatCalcFormPopup = function()
    {
        this.hideMask();
        this.entryFormPopup.style.display = "none";
    }

    // show the about popup
    popup.showAboutPopup = function()
    {
        this.showMask();
        this.aboutPopup.style.display = "block";
        this.positionDialogue(this.aboutPopup);
    }

    // hide about popup
    popup.hideAboutPopup = function()
    {
        this.hideMask();
        this.aboutPopup.style.display = "none";
    }

    // position dialogue center screen
    popup.positionDialogue = function(popupBox)
    {
        popupBox.style.left = (($(document).width() / 2) - (popupBox.offsetWidth / 2)) + "px";
    }

    popup.calculate = () =>{

        //Getting reuqired values
        let age = document.getElementById("Age").value;
        let weight = document.getElementById("Weight").value;
        let sex = document.querySelector('input[name="sex"]:checked').value;
        let cr = document.getElementById("serum").value;
        //Using a boolean flag whether the sex is female
        let isFemale = sex === 'f' ? true : false;

        //Processing values through the formula
        let result = popup.processValues(age,weight,isFemale,cr)

        //Inserting result element in the DOM
        let element = document.getElementById("br");
        let newElement = `<p id="result">CrCl : ${result}</p>`
        element.insertAdjacentHTML( 'afterend', newElement )
    }

    popup.processValues = (age,weight,isFemale,cr) => {
        let genderFactor = isFemale ? 0.85 : 1;
        return (140-age)*weight*genderFactor/(72*cr)
    }

    return popup;
}
